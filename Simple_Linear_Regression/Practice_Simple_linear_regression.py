# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:35:34 2017

@author: RGautam
"""
import numpy as np
import matplotlib.pyplot as mplot
import pandas as pd


data = pd.read_csv('Salary_data.csv')

X = data.iloc[:,:-1].values
Y = data.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train, Y_test =  train_test_split(X,Y,test_size = 1/3, random_state = 0) 


#train the model using training data
from sklearn.linear_model import LinearRegression
regressor =  LinearRegression()
regressor.fit(X_train,Y_train)

#predict the Y
y_pred = regressor.predict(X_test) 

#Visualizing the training set results
mplot.scatter(X_train , Y_train, color='red')
mplot.plot(X_train, regressor.predict(X_train), color = 'blue')
mplot.title('Salary vs Experience( Training Set)')
mplot.xlabel('Experience in Years')
mplot.ylabel('Salary')
mplot.show()

#Visualizing the Tst set result
mplot.scatter(X_test, Y_test, color='Green')
mplot.plot(X_train, regressor.predict(X_train), color = 'blue')
mplot.title('Test Data visulaization')
mplot.xlabel('Experience in Years')
mplot.ylabel('Salary')
mplot.show()