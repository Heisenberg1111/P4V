#!/usr/bin/python3

# Use the train test slip functionality of scikit-learn module


from sklearn import datasets
import numpy as np

from sklearn.model_selection import train_test_split

iris=datasets.load_iris()

X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
