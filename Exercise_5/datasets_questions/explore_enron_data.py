#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

# enron_data is a dictionary
enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

# print the enron_data dictionary
print(enron_data)

# Number of people
print(len(enron_data))

# For each person, number of feature
print(len(enron_data['METTS MARK']))

# Finding number of POIs
numberOfPOI = 0
for key in enron_data:
    print(key)
    if enron_data[key]["poi"] == True:
        numberOfPOI += 1

        #print((enron_data[key]["poi"]))

print(numberOfPOI)

# Finding number of POIs exists
#POIsExist = open("../final_project/poi_names.txt", "rb")

#print(POIsExist)

# Finding total stock value of James Prentice
print((enron_data['Prentice James'.upper()]['total_stock_value']))

# How many email messages do we have from Wesley Colwell to persons of interest?
print((enron_data['Colwell Wesley'.upper()]['from_this_person_to_poi']))

# What’s the value of stock options exercised by Jeffrey K Skilling?
print((enron_data['Skilling Jeffrey K'.upper()]['exercised_stock_options']))

# Lay, Skilling and Fastow, who took home the most money (largest value of “total_payments” feature)?
# How much money did that person get?

print("LAY KENNETH L, total_payments : ", (enron_data['LAY KENNETH L'.upper()]['total_payments']))
print("Skilling Jeffrey K, total_payments : ", (enron_data['Skilling Jeffrey K'.upper()]['total_payments']))
print("FASTOW ANDREW S, total_payments : ", (enron_data['FASTOW ANDREW S'.upper()]['total_payments']))

# How many folks in this dataset have a quantified salary? What about a known email address?
# salary
# email_address

numberOfQuantifiedSalary = 0
numberOfKnownEmailAddress = 0
for key in enron_data:
    #print(key)
    if enron_data[key]["salary"] != 'NaN':
        numberOfQuantifiedSalary += 1

    if enron_data[key]["email_address"] != 'NaN':
        numberOfKnownEmailAddress += 1

print("numberOfQuantifiedSalary : ", numberOfQuantifiedSalary)
print("numberOfKnownEmailAddress : ", numberOfKnownEmailAddress)

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?

numberOfTotalPaymentsHaveNaN = 0
numberOfKey = 0
for key in enron_data:
    numberOfKey += 1
    #print(key)
    if enron_data[key]["total_payments"] == 'NaN':
        numberOfTotalPaymentsHaveNaN += 1

print("numberOfTotalPaymentsHaveNaN : ", numberOfTotalPaymentsHaveNaN)
print("numberOfKey : ", numberOfKey)
print("percentage of people in the dataset have NaN for their total_payments : ", numberOfTotalPaymentsHaveNaN * 100 / numberOfKey)

# How many people in the E+F dataset (as it currently exists) have “NaN” for their POIs? What percentage of people in the dataset as a whole is this?

numberOfPOIsHaveNaN = 0
#numberOfPOI = 0
numberOfKey = 0
for key in enron_data:
    numberOfKey += 1
    #print(key)
    #if enron_data[key]["poi"] == True :
        #numberOfPOI += 1
    if enron_data[key]["poi"] == 'NaN':
        numberOfPOIsHaveNaN += 1

print("numberOfPOIsHaveNaN : ", numberOfPOIsHaveNaN)
#print("numberOfPOI : ", numberOfPOI)
print("numberOfKey : ", numberOfKey)
print("percentage of people in the dataset have NaN for their POI : ", numberOfPOIsHaveNaN * 100 / numberOfKey)

# If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.
# What is the new number of people of the dataset?
# 146 + 10 = 156
# What is the new number of folks with “NaN” for total payments?
# 21 + 10 = 31

# Finding # What is the new number of POI’s in the dataset? and What is the new number of POI’s with NaN for total_payments?
numberOfPOIsHaveNaN = 0
numberOfPOI = 0
numberOfKey = 0
numberOfPOIsHaveNaNInTheirTotalPayments = 0
for key in enron_data:
    numberOfKey += 1
    #print(key)
    if enron_data[key]["poi"] == True :
        numberOfPOI += 1
        if enron_data[key]["total_payments"] == 'NaN':
            numberOfPOIsHaveNaNInTheirTotalPayments += 1

print("numberOfPOIsHaveNaNInTheirTotalPayments : ", numberOfPOIsHaveNaNInTheirTotalPayments)
print("numberOfPOI : ", numberOfPOI)
#print("numberOfKey : ", numberOfKey)
print("percentage of people in the dataset have NaN for their POI : ", numberOfPOIsHaveNaNInTheirTotalPayments * 100 / numberOfPOI)

# What is the new number of POI’s in the dataset?
# 18 + 10 = 28
# What is the new number of POI’s with NaN for total_payments?
# 0 + 10 = 10

# Once the new data points are added, do you think a supervised classification algorithm might interpret “NaN” for total_payments as a clue that someone is a POI?
# YES