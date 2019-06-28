# Recommendation_System
Chirag Shah

In this project, a recommender system is built with use of NLTK, scikit, and numpy.

We have made use of the movie.json file to train from Amazon's Movie Review Data available on Kaggle or download it from here: http://jmcauley.ucsd.edu/data/amazon/.

○ main.py splits it for train dataset (80%) and dev dataset (20%) which will train the recommender system.
○ Recommender.py works on the trained set and expects output for the user:
○ Expected output
 User-based recommender system MAE: x.xx (ex. 1.03)
or Item-based recommender MAE: x.xx
or  Contents-based recommender MAE: x.xx
or  Best recommender system MAE: x.xx
