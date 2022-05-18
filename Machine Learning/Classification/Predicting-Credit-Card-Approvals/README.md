# Predicting-Credit-Card-Approvals
![image](https://user-images.githubusercontent.com/83561056/160240803-24928c01-2a71-4256-86a4-14c081193761.png)



## Credit card applications.
Commercial banks receive a lot of applications for credit cards. 
Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. 
Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). 
Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. 

In this notebook, we will build an automatic credit card approval predictor using machine learning techniques, just like the real banks doing 

Credit Card Approval dataset from the UCI Machine Learning Repository. 
The structure of this notebook is as follows:
First, we will start off by loading and viewing the dataset. We will see that the dataset has a mixture of both numerical and non-numerical features, that it contains values from different ranges, plus that it contains a number of missing entries.We will have to preprocess the dataset to ensure the machine learning model we choose can make good predictions.After our data is in good shape, we will do some exploratory data analysis to build our intuitions.

Finally, we will build a machine learning model that can predict if an individual's application for a credit card will be accepted.
First, loading and viewing the dataset. We find that since this data is confidential, the contributor of the dataset has anonymized the feature names.
