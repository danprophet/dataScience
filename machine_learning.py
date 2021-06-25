"This file will handle the machine learning part of the projectimport pandas as pd"
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt
import const_variables as const


def create_decision_tree(data):
    """
    This function creates your decision tree according to the information your want to predict.
    :param: data - the dataframe
    """
    while True:
        print("Do you want to create new decision tree? (Y/N)")
        answer = input()
        if answer == 'Y':
            columns_for_predictions = []
            print("Please enter your requested columns for your question, press E to end reading: \n"
                  "The possible columns in the database are:")
            for column in data.columns:
                # Print list of columns with description
                print('{} - {}'.format(column, (const.columns_description['columns'])[column]))

            for i in range(len(data.columns)):
                columns_name = input()
                if columns_name == 'E':
                    break
                if columns_name not in data.columns:
                    print("column does not exist, try again.")
                else:
                    columns_for_predictions.append(columns_name)

            while True:
                print("Please enter the columns you would like to predict: \n")
                predict_column = input()
                if predict_column not in data.columns:
                    print("Columns does not exist, try again.")
                else:
                    print("You chose to use {} to preict {}. \n desicion tree execution stated...".format(columns_for_predictions, predict_column))
                    create_prediction(data, columns_for_predictions, predict_column)
                    break
        else:
            break  # Kill loop.


def create_prediction(data, columns1, column2):
    ###Constructing Data Frame
    decisionTree = tree.DecisionTreeClassifier()

    ###Splitting train/test data
    print("Splitting the data.. \n")
    x=data[columns1]
    y=data[column2]
    X_tr, X_ts, y_tr, y_ts = tts(x, y, test_size=20/100, random_state=None)

    ###Creating Decision Tree Classifier Model
    print("Creating decision Tree.. \n")
    decisionTree = decisionTree.fit(X_tr, y_tr)
    fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (30,30), dpi=600)

    tree.plot_tree(decisionTree)
    fig.savefig('machine_learning_trees/decision_tree_{}_to_{}.png'.format(columns1, column2))
    print('machine_learning_trees/decision_tree_{}_to_{}.png Created.\n'.format(columns1, column2))

    ###Training the Model
    print("Training the Model...\n")
    decisionTree.fit(X_tr,y_tr)

    ###Making Predictions
    print("Making Predictions...\n")
    y_pr=decisionTree.predict(X_ts)

    ###Evaluating Prediction Accuracy
    print("Your Model Accuracy is %:", metrics.accuracy_score(y_ts, y_pr)*100)

    ###Making Prediction with Foreign Data
    # while loop to make predictions:
    while True:
        print("Do you want to predict? (Y/N)")
        answer = input()
        if answer == 'Y':
            answer_vector = []
            print("Please enter your data for predition:\n "
                  "you should enter in the following format: {}".format(columns1))
            for i in range(len(columns1)):
                a = input()
                answer_vector.append(a)

            predictions = decisionTree.predict([answer_vector])  # send predictions

            print("---------------\n Your prediction is: {}\n---------------".format(predictions))
        else:
            break  # Kill loop.



