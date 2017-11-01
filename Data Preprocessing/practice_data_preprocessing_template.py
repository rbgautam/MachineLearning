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
