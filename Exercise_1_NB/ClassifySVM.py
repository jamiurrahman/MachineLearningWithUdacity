# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:20:13 2019

@author: Orin
"""

def classify_SVM(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    import numpy as np
    
    from sklearn.svm import SVC
    clf = SVC(C=1000.0, kernel='rbf')
    clf.fit(features_train, labels_train)
    return clf