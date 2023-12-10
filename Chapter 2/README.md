# Supervised Learning
-> It is one of the commonly used and successful types of machine learning.
-> Supervised learning is used to predict the outcome of a given event when we have input/output pairs. Our goal is to make predictions for new, never-seen-before-data.

## Classification and Regression
    -> There are two major types of Supervised machine Learning problems, classification and regression. 
    -> In classification, the goal is to predict a class label, which is a list of predifined possibilities.
    Classification can be sometimes be separated into binary classification, which is the distinguishes between two classes, and multiclass which is more than two classes.
    Binary classification is a yes/no question, positive/negative class. 
    -> In Regression, the goal is to predict a continous number/floating point number/real number.

    -> However, do differentiate between the two, is to ask whether there is some kind of continuity in the output. For example the iris problem is classification since the species cannot            change while in regression predicting income can change with time(iykyk).

### Generaliaztion, Overfitting, and Underfitting
    -> If a model is able to make predictions from unseen data, we say it is able to generalize from the training data to the test data/set. The goal is build a model that is able to generalize as accurately as possible.

    -> The only measure an algorithm will perform well on a new data is the evaluation on the test set.

    -> Overfitting occurs when you fit a model too closely to the particularities of the training set and obtain a model that works well on the training set but is not able to generalize to new data. Underfitting on the other hand is chossing a too simple model. The more complex we allow our model to be, the better we will be able to predict on the training data. however, this will lead to too much focusing on each individual data point in our training set, and the model will not generalize well to new data.

### Relation of Model Complexity to Dataset Size
    -> Its important to note that model complexity is tied to the variation of inputs contained in your training dataset: the larger the variety of data points the more complex a model you can use without overfitting.

    ### Supervised Machine Learning Algorithms
    -> A review of the most popular machine learning algorithms and how they learn from data and make predictions and discuss how model complexity play out for each of these models.

    k-Nearest Neighbors
    -> Arguably the simplest machine learning algorithm. To make predictions for a new data point, the algorithm finds the closest data points in the training dataset--its nearest neighbors.

    k-Neighbors classification
    ->In this it only considers exactly one nearest neighbor, which is the closest training data point to the point we want to make the prediction(output).
    ->Instead of considering only one closest neighbor, we can consider an arbitrary number, k, of neighbors(the name of the algorithm is basedon this actually). We use voting to assign a label, voting in that we assign class that is more frequent among the k-nearest neighbors. 

    
