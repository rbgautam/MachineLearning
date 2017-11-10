#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:24:16 2017

@author: Deltaman
"""
import numpy as np
import matplotlib.pyplot as mplot
import pandas as pd

sampledata =  pd.read_csv('50_Startups.csv')
X = sampledata.iloc[:,:-1].values
y = sampledata.iloc[:,4].values



from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lblEncoderX =  LabelEncoder()
X[:,3] =  lblEncoderX.fit_transform(X[:,3])

oneHotEnc =  OneHotEncoder(categorical_features = [3])
X= oneHotEnc.fit_transform(X).toarray()

#Removing Extra encoded data (Always use -1 total Encoded columns eg: if 3 then use 2, if 4 then use 3  )
X = X[:,1:]


#Split data into Training And validation 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train, y_test =  train_test_split(X,y, test_size = 0.2,random_state = 0)

# fitting the model to Linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

#try to get better at plotting data
# =============================================================================
# mplot.scatter(X_test[:,2], y_pred)
# mplot.plot(X_test[:,2],y_test)
# mplot.title('Test Data vs Test Pred')
# mplot.xlabel('R&D Expenditure')
# mplot.ylabel('Profit Prediction') 
#  
# =============================================================================
