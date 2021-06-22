"This file will handle the machine learning part of the projectimport pandas as pd"

###Importing Libraries
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt


def create_prediction(data, columns1, column2):
    ###Constructing Data Frame
    decisionTree = tree.DecisionTreeClassifier()

    ###Splitting train/test data
    x=data[columns1]
    y=data[column2]
    X_tr, X_ts, y_tr, y_ts = tts(x, y, test_size=20/100, random_state=None)

    ###Creating Decision Tree Classifier Model
    # DT = DTC()
    decisionTree = decisionTree.fit(X_tr, y_tr)
    fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (30,30), dpi=600)

    tree.plot_tree(decisionTree)
    fig.savefig('machine_learning_trees/decision_tree_{}_to_{}.png'.format(columns1, column2))
    #
    ###Training the Model
    decisionTree.fit(X_tr,y_tr)

    ###Making Predictions
    y_pr=decisionTree.predict(X_ts)

    ###Evaluating Prediction Accuracy
    print("Acc %:", metrics.accuracy_score(y_ts, y_pr)*100)

    ###Making Prediction with Foreign Data
    # while loop to make predictions:

    # while True:
    #     print("Enter {}".format(columns1))
    #     decisionTree.predict(decisionTree, ['state', 'lgt_cond', 'hour'], ['fatals'])


