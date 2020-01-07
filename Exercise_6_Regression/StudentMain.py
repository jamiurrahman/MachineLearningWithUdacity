#!/usr/bin/python

import numpy
import matplotlib
#matplotlib.use('agg')
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from StudentRegression import studentReg
from ClassVis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

print(ages_test.shape)
print(net_worths_test.shape)

reg = studentReg(ages_train, net_worths_train)

# printing some information from my fitted regression line
# y = mx + c
print("reg slope (m) : ", reg.coef_)
print("reg offset (c) : ", reg.intercept_)

# working with score (r-squared score)
# r-squared score for training data is not useful
print("r-squared score for training data: ", reg.score(ages_train, net_worths_train))

# r-squared score for testing data is very useful
print("r-squared score for testing data: ", reg.score(ages_test, net_worths_test))


plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.interactive(False)
print(plt.isinteractive())
#plt.imshow()
#plt.show(block=True)

plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
