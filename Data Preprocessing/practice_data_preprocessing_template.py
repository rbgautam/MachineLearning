#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:46:31 2017

@author: Deltaman
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#import the dataset
dataset = pd.read_csv('data.csv')

features = dataset.iloc[:,:-1].values
#set np.set_printoptions(threshold =np.nan) to show all data in console

output = dataset.iloc[:,3].values


#Handling the missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(features[:,1:3])
features[:,1:3] = imputer.transform(features[:,1:3])

#Handling categories for input
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_feature = LabelEncoder()
features[:,0] = labelencoder_feature.fit_transform(features[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
features = onehotencoder.fit_transform(features).toarray()
#Handling categories for output
labelencoder_output =  LabelEncoder()
output = labelencoder_output.fit_transform(output)

#Data splitting for Training and testing

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test= train_test_split(features, output,test_size = 0.2, random_state = 0) 

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)