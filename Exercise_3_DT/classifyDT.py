# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:39:54 2019

@author: Orin
"""

from sklearn import tree

def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    clf = tree.DecisionTreeClassifier(min_samples_split = 50)
    clf.fit(features_train, labels_train)
    
    
    return clf