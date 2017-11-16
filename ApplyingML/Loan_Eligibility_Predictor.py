# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:18:28 2017

@author: RGautam
"""

import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

#getting header data

headerData = list(pd.read_csv('german_data_column_names.txt')) 
sampledata = pd.DataFrame(pd.read_csv('german_credit_data.csv', names= headerData))

#Split into featureset and result
X = sampledata.iloc[:,:-1].values
y = sampledata.iloc[:,20].values

#Encode Catagorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encode_col =  LabelEncoder()
cols_to_be_encoded = [0,2,3,5,6,8,9,11,13,14,16,18,19]

for col in cols_to_be_encoded:
    X[0:,col] = encode_col.fit_transform(X[0:,col])

#OneHotEncoding 
df_with_dummies = pd.get_dummies( pd.DataFrame(X)  , columns = cols_to_be_encoded)    
X = df_with_dummies.values



#Test data and Train Dta splitting
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 0 ) 

#Feature Scaling
#from sklearn.preprocessing import StandardScaler
#X_scale = StandardScaler()
#X_train =   X_scale.fit_transform(X_train)
#X_test = X_scale.fit_transform(X_test)

#Model Training 
###INMPOERTANT : DOD NOT USE lINEAR REGRESSION IN THIS PROBLEM AS ITS A CLASSIFICATION PROBLEM
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#Prediction validation
y_pred = regressor.predict(X_test)

#Compare results





 