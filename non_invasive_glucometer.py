# -*- coding: utf-8 -*-
"""Non Invasive glucometer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SZUa6vUyNk-x160fMRSE7pMjlJeDIPLu
"""

!pip install Pyrebase

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats
import statsmodels.api as sm

x = np.array([1513,1552,1623,1560,1615,1575,1705,1501,1523,1616,1635,1555,1620,1497,1540,1640,1576,1630])
y = np.array([92,61,106,100,108,73,131,84,80,119,129,93,125,81,73,122,98,110])

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.xlabel("Voltage")
plt.ylabel("Glucose Concentration")
plt.show()

print("\nThe relation value is ",round((r*100),2),"%")   # The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.

#Glucose = myfunc(float(input("Enter the Voltage: ")))
#print("The Glucose Value is ",Glucose)

Glucose = myfunc(float(input("Enter the Voltage: ")))
print("The Glucose Value is ",Glucose)

import pyrebase

firebaseConfig = {"apiKey": "AIzaSyBVYvmv2IUJy-d-jxKKsjbgMcnfLOX8_ns",
  "authDomain": "something-unique-10986.firebaseapp.com",
  "databaseURL": "https://something-unique-10986-default-rtdb.firebaseio.com",
  "projectId": "something-unique-10986",
  "storageBucket": "something-unique-10986.appspot.com",
  "messagingSenderId": "557386094587",
  "appId": "1:557386094587:web:47bd8eb129106a60d6dd5e",
  "measurementId": "G-ZLQQWEZD9B"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data={"Value":Glucose}

db.child("Name").set(data)