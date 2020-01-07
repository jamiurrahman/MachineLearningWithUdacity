#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
from outliers.feature_format import featureFormat, targetFeatureSplit


from outliers.feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("final_project_dataset_unix.pkl", "rb") )

dictionary.pop('TOTAL',0)

### list the features you want to look at--first item in the
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.1, random_state=42)
train_color = "b"
test_color = "r"

print(feature_test)
print(target_test)

### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

from sklearn.linear_model import LinearRegression

reg = LinearRegression(fit_intercept=True)
reg.fit(feature_train, target_train)
#reg.fit(feature_test, target_test)
#reg.fit(features, target)

#reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# What are the slope and intercept?
print("Slope : ", reg.coef_)
print("Intercept : ", reg.intercept_)

# working with score (r-squared score)
# r-squared score for training data is not useful
print("r-squared score for training data: ", reg.score(feature_train, target_train))

# r-squared score for testing data is very useful
print("r-squared score for testing data: ", reg.score(feature_test, target_test))




### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color )
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color )

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()


### identify and remove the most outlier-y points


from outliers.outlier_cleaner import outlierCleaner
cleaned_data = []
try:
    predictions = reg.predict(feature_train)
    cleaned_data = outlierCleaner( predictions, feature_train, target_train )
except NameError:
    print("your regression object doesn't exist, or isn't name reg")
    print("can't make predictions to use in identifying outliers")





import numpy

### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")

        # What are the slope and intercept?
        print("Slope after cleaned data : ", reg.coef_)
        print("Intercept after cleaned data : ", reg.intercept_)

        # working with score (r-squared score)
        # r-squared score for training data is not useful
        print("r-squared score for training data after cleaned data : ", reg.score(feature_train, target_train))

        # r-squared score for testing data is very useful
        print("r-squared score for testing data after cleaned data : ", reg.score(feature_test, target_test))
    except NameError:
        print("you don't seem to have regression imported/created,")
        print("   or else your regression object isn't named reg")
        print("   either way, only draw the scatter plot of the cleaned data")
    plt.scatter(ages, net_worths)
    plt.xlabel("Salary")
    plt.ylabel("Bonus")
    plt.show()


else:
    print("outlierCleaner() is returning an empty list, no refitting to be done")

