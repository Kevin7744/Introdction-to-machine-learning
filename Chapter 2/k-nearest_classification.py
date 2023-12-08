from skilearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Import and instatiate the class 
# set the params of the nearest neighbor to use.
from skilearn.neighbors import kNeighborsClassifier
clf = kNeighborsClassifier(n_neighbor = 3)

# fit the classifier using the training set
clf.fit(X_train, y_train)

# Call predict method to make predictions
print("Test set predictions: {}".format(clf.predict(X_test)))

# Evaluate how well the model generalizes
# Call the score method together with test labels
print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))

