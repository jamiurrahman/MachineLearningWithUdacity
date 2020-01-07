#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
#sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(C=10000.0, kernel="rbf")


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data

# =============================================================================
# SVM takes too much time if the dataset is big
# This is how we can take 1% of the whole dataset, but the accuracy goes done from 98.4% to 61%
# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]
# =============================================================================

clf.fit(features_train, labels_train)


#### store your predictions in a list named pred
pred = clf.predict(features_test)


# =============================================================================
# For extra work on the udacity answers
# pred2 = clf.predict(features_test)
# 
# pred2[10]
# Out[43]: 1
# 
# pred2[26]
# Out[44]: 0
# 
# pred2[50]
# Out[45]: 1
# 
# np.count_nonzero(pred)
# Out[46]: 877
# =============================================================================


from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print(acc)

def submitAccuracy():
    return acc

#########################################################


