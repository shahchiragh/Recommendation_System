#Author: Chirag Shah
#UTA ID: 1001558824


#Recommender.py to train the recommender system..
import pandas as pd 
import numpy as np
import math

#Read train.csv which was created from main program..
df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
train_matrix= df.set_index(['reviewerID_x'])
test_matrix = test_df.set_index(['reviewerID_x'])



#Creating Movie matrix using Pivot Table
#train_matrix = pd.pivot_table(df, index='reviewerID_x', columns='asin', values='overall_x')

#create dataframe of top 2 movies from moview_matrix.
##B003EYVXV4  4.108816               1985
##B001KVZ6HK  4.524364               1888
##B009934S5M  4.317601               1801
##B0059XTU1S  4.254777               1570
##B005LAIHXQ  3.565541               1480
##B005LAIIMG  3.691063               1421
##B00AF6B22E  3.843705               1382
##B00FZM8Z7I  4.546512               1376
##B00H83EUL2  3.665175               1341
##B002VPE1AW  4.115385               1326

#top_ten_reviewed_products = {'B003EYVXV4','B001KVZ6HK', 'B009934S5M', 'B0059XTU1S','B005LAIHXQ', 'B005LAIIMG' , 'B00AF6B22E', 'B00FZM8Z7I', 'B00H83EUL2', 'B002VPE1AW'}
top_five_reviewed_products = ['B003EYVXV4','B001KVZ6HK', 'B009934S5M', 'B0059XTU1S','B005LAIHXQ']

#train_product_1 = train_matrix['B003EYVXV4']

Mean_Absoulte_Error=0
for i in top_five_reviewed_products:
    #print("Product:",i)
    train_product = train_matrix[i]
    products_similar_to_product = train_matrix.corrwith(train_product)
    
    users_who_rated = test_matrix[i]#A1GZP6A3EYGY90
    users_who_rated.dropna(inplace=True)
    get_five_users = users_who_rated[0:5]
    for p,actual_rating in zip(get_five_users.index.values,get_five_users):
        print("\nUser:",p)
        user_matrix = test_df.loc[test_df['reviewerID_x']== p].dropna(axis='columns').iloc[0][1:]
        #print(user_matrix)
        denom=0
        for k in user_matrix.index.values:
            if(k!=i):
                #print(k,"has:",products_similar_to_product[k],"\n")
                sim_value=products_similar_to_product[k]
                if(math.isnan(sim_value)):
                    non_nan = 0
                else:
                    non_nan = sim_value
                denom+=non_nan

        numer=0
        for l,m in zip(user_matrix,user_matrix.index.values):
            #print(l,m,"\n")
            if(l!=i and m!=i):
                sim_value=products_similar_to_product[m]
                if(math.isnan(sim_value)):
                    non_nan = 0
                else:
                    non_nan = sim_value
                numer+=non_nan*l
        if(denom == 0 and numer ==0):
            prediction=0
        else:
            prediction=numer/denom
        if(prediction>5.0):
            prediction = 5.0
        #print("User: ",p)
        #print("Prediction: ",prediction)
        #print("Actual: ",actual_rating)
        #print("Error: ",prediction - actual_rating)
        Mean_Absoulte_Error += abs(prediction - actual_rating)
        #print("Predcition:",prediction," Error:", Mean_Absoulte_Error)
        
print("Item-based recommender MAE: ",Mean_Absoulte_Error/25,"\n")




#user_matrix.dropna(inplace=True)
##test_product_1 = test_matrix['B003EYVXV4']#A1GZP6A3EYGY90
##test_product_1.dropna(inplace=True)
##
##user_matrix = test_df.loc[test_df['reviewerID_x']=='A2A5J21CI40RKT'].dropna(axis='columns').iloc[0][1:]
##
##denom=0
##for i in user_matrix.index.values:
##    if(i!='B003EYVXV4'):
##        print(i,"has:",products_similar_to_product_1[i])
##        denom+=products_similar_to_product_1[i]
##
##numer=0
##for i,j in zip(user_matrix,user_matrix.index.values):
##    print(i,j)
##    if(i!= 'B003EYVXV4'and j!='B003EYVXV4'):
##        numer+=products_similar_to_product_1[j]*i

#A1Y32TS3DEGCAA
#prediction =

            
##product_2 = movie_matrix['B001KVZ6HK']
##
#products_similar_to_product_1= train_matrix.corrwith(train_product_1)
##products_similar_to_product_2= movie_matrix.corrwith(product_2)
##
##correlation_product_1 = pd.DataFrame(products_similar_to_product_1,columns=['Correlation'])
##correlation_product_1.dropna(inplace=True)
###correlation_product_1.sort_values(by='Correlation',ascending=False)
##correlation_product_2 = pd.DataFrame(products_similar_to_product_2,columns=['Correlation'])
##correlation_product_2.dropna(inplace=True)
#correlation_product_2.sort_values(by='Correlation',ascending=False)


#product_list=np.array(df.columns.values)[1:]
#Get total Count of products
#total_products = len(product_list)
#intialized empty Adjusted Sim Matrix
#AdjSimMatrix=np.empty([total_products,total_products])
