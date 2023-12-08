# Chapter 1

This chapter goes through the essential Libraries and tools used in ML, these tools include
Jupiter Notebook
An interactive environment for running code in the browser. It makes it easy to incorporate code, text, and images.

    Numpy
    One of the fundamental packages for scientific computing in python

    SciPy
    Is a collection of functions for scientific computing

    Matplotlib
    Is the primary scientific plotting library in python

    Pandas
    is a python library for data wrangling and analysis.

    mgLearn

    python3(recommended)

# A First application: Classifying iris species

->The length and width of petals and sepals of different iris       flowers are collected and the measurements recorded. Measurements of previously collectecd flowers are available so we can certain which each species each iris belongs to.
->The ML model will learn from this measurements(The known       measurements), so we can predict the species for a new iris. This  is a supervised learning problem and classification problem since we are predicting a species of iris(classes).
->The measurements of some of the irises are species setosa, versicolour, or virginica. Every iris in the dataset belongs to one of the three classes, so this problem is a three-classification problem.
->The data used is the iris dataset included in the scikit-learn datasets module
->The species are encoded as integers from 0 to 2. 0 means setosa, 1 means versicolour and 2 virginica. 
->Training and Testing data, assume this scenario, you learn a new topic on math and to test your understanding, instead of doing the examples you worked with while learning, you search for new questions on the same topic for your understanding. This is the same case for ML, data is split into training and test data. scikit-learn contains a function that shuffles the dataset and spits it for you. the  'train_test_split' funtion. It extract 75% as training set and 25% as test data. We shuffle our data to make sure the test data contains data from all classes.
->In scikit-learn data is denoted with a capital X and labels with lowecase y.