import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier



iris_dataset = load_iris()
print("Keys of iris_datasets: \n{}".format(iris_dataset.keys()))
# DECR key is a short description of the dataset
print(iris_dataset['DECR'][:193] + "\n...")
# target_names key is an array of strings, coontaining the species
# flower we want to predict
print("Target names: {}".format(iris_dataset['target_names']))
# Feature_names key is a list of strings giving a description of each feature
print("Feature names: \n{}".format(iris_dataset['feature_names']))
# The data is in the data and target keys with a numpt array
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))
# Feature of the first five values
print("First five columns of data:\n".format(iris_dataset['data'][:5]))
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))
# species are encoded as integers from 0 to 2.
print("Target:\n{}".format(iris_dataset['target']))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
print("X_train shape:{}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape: {}".format(X_new.shape))
# to make predictions 
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))

# predictiona accuracy
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
