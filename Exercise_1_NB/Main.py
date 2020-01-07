# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:17:51 2019

@author: Orin
"""

#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify
from sklearn.metrics import accuracy_score

import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classify(features_train, labels_train)

#print('The result for the prediction is: ', clf.predict(features_test))

pred = clf.predict(features_test)

print('The accuracy of my prediction is : ', accuracy_score(labels_test, pred))

print('The from the clf.score is : ', clf.score(features_test, labels_test))

counterClassifiedCorrectly = 0
for i in range(0, len(features_test)):
    if (labels_test[i] == pred[i]):
        counterClassifiedCorrectly += 1
        
myAcccuracy = counterClassifiedCorrectly / len(features_test)
print('My Calculated accuracy is : ', counterClassifiedCorrectly, len(features_test), myAcccuracy)

accuracy_score(labels_test, pred)


### draw the decision boundary with the text points overlaid
# =============================================================================
# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())
# =============================================================================





"""Working with SVM Classifier"""
from class_vis import prettyPicture_SVM
from ClassifySVM import classify_SVM
clf_SVM = classify_SVM(features_train, labels_train)

#print('The result for the prediction is: ', clf.predict(features_test))

pred_SVM = clf_SVM.predict(features_test)

print('The accuracy of my SVM prediction is : ', accuracy_score(labels_test, pred_SVM))


counterClassifiedCorrectly = 0
for i in range(0, len(features_test)):
    if (labels_test[i] == pred_SVM[i]):
        counterClassifiedCorrectly += 1


### draw the decision boundary with the text points overlaid
prettyPicture_SVM(clf_SVM, features_test, labels_test)
#output_image("test_SVM.png", "png", open("test_SVM.png", "rb").read())

