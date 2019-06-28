#Author: Chirag Shah
#UTA ID: 1001558824

#scrip starts
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
#from scipy.sparse import csr_matrix

#import warnings
#warnings.filterwarnings('ignore')

#preprocess json file to CSV 
##json_movie=pd.read_json('movie.json')
##filter_json_movie = json_movie[['reviewerID','asin','overall']]
##filter_json_movie.to_csv('movies.csv',index=False)

#Conversion from JSON to CSV takes more than 4 mins in my given laptop..
#So I have already converted it into CSV AND I am going to use and read from the same file
#for further development
df = pd.read_csv('movie.csv')


#to get a brief on the data -- uncomment below line
#df.describe()

#To get overall products with highest number of ratings..
ratings = pd.DataFrame(df.groupby('asin')['overall'].mean())
ratings['number_of_ratings'] = df.groupby('asin')['overall'].count()
#Use below line and pass it in console to get top 10 values..
top_list=ratings.sort_values('number_of_ratings', ascending=False).head(10)


#ratings['number_of_ratings'] = df.groupby('asin')['overall'].count()
#ratings.head()
#ratings['overall'].hist(bins=50)
#ratings['number_of_ratings'].hist(bins=60)
#sns.jointplot(x='overall', y='number_of_ratings', data=ratings)
#movie_matrix = pd.pivot_table(train, index='reviewerID', columns='asin', values='overall',aggfunc=np.mean)


###A NEW APPROACH
#Get count of individual products that have rated in the entire dataset by users
count = df.groupby("asin", as_index=False).count()
#Get mean of the individal products to get and average rating on that product
mean = df.groupby("asin", as_index=False).mean()
#Merge the count of individual products to primary Dataframe..
df_Merged = pd.merge(df, count, how='right', on=['asin'])
#Renaming few column names for simplicity..
df_Merged["totalReviewers"] = df_Merged["reviewerID_y"]
df_Merged["overallScore"] = df_Merged["overall_x"]
#df_final_New = df_Merged[['asin','overallScore',"totalReviewers"]]

#Lets sort product which is highly reviewed..
df_Merged = df_Merged.sort_values(by='totalReviewers', ascending=False)

#Keeping threshold of minimum 250 reviews on product..
df_Filtered = df_Merged[df_Merged.totalReviewers >= 250]

#Generating a Pivot Matrix from filtered Dataframe..
movie_matrix = pd.pivot_table(df_Filtered, index='reviewerID_x', columns='asin', values='overall_x')

train, test = train_test_split(movie_matrix, test_size=0.2)

#Calling Train.py to Train our Recommender System..


#Calling Test.py to Test our Recommender System..

#based on this train and test data we are creating our Recommender System..
#Write Train.csv and Test.csv

train.to_csv('train.csv')
test.to_csv('test.csv')


#printin in to CSV..
#dfCount.to_csv('ReviewSummary.csv')
#dfc =dfCount.groupby(['reviewerID_x']).count()
#dfProductReview = df.groupby("asin", as_index=False).mean()
#movie_matrix.to_csv('Pivoted_Matrix.csv',index=False)
#ratings['number_of_ratings'] = df.groupby('asin')['overall'].count()







