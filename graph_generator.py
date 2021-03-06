"This python file will handle processing csv data to different graphs"
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import const_variables as consts
# %matplotlib inline  # ???


def bar_graph_to_file(df, column1, column2):
    """
    This function generates bar graph to PNG file, according to give column1 & column2
    :param df: given DataFrame
    :param column1: X axis column
    :param column2: Y axis column
    """
    table = pd.crosstab(df[column2], df[column1])
    table.plot(kind='bar', figsize=(20, 15))
    plt.title("{} vs. {}".format(column1, column2))
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.legend(consts.columns_description[column1])
    plt.savefig('graphs/bar_graphs/{}_vs_{}.png'.format(column1, column2))
    plt.clf()


def scatter_plot_graph_to_file(df, x_column, y_column):
    """
    This function generates base_column to columns_list average graph to PNG file
    :param df: given DataFrame
    :param categorical_column: base columns to be compared to
    :param x_column: columns to be compared with base_column (average)
    :param y_column: columns to be compared with base_column (average)
    """
    df.plot.scatter(x=x_column, y=y_column, alpha=0.5, figsize=(200, 100))
    plt.title("scatter plot - categorical_column {} vs. {}".format(x_column, y_column))
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig('graphs/scatter_plots/scatter_plot_{}_vs_{}.png'.format(x_column, y_column))
    plt.clf()


def pie_graph(df, column):
    """
    This function generates graph of years vs cases
    :param df:
    :return:
    """
    fig = plt.figure(figsize=(30, 30))
    try:
        df[column].value_counts(sort=False).plot(kind='pie', autopct="%.2f", labels=consts.columns_description[column])
    except Exception as e:
        df[column].value_counts().plot(kind='pie', autopct="%.2f", labels=None)


    try:
        plt.legend(consts.columns_description[column])
    except Exception as e:
        print("Column data not found. \n{}".format(e))

    plt.title("{} Pie Graph".format(column))
    plt.savefig('graphs/pie/{}_graph_pie.png'.format(column))
    plt.clf()


def general_overview(df, column):
    """
    This function generates general graph
    :param df:
    """
    df.plot()
    try:
        plt.legend(consts.columns_description[column])
    except Exception as e:
        print("Column data not found. \n{}".format(e))

    plt.title("{} General Graph".format(column))
    plt.savefig('graphs/{}_graph_general_overview.png'.format(column))


def general_overview_column(df, column):
    """
    This function generates general graph
    :param df:
    """
    df[column].plot()
    try:
        plt.legend(consts.columns_description[column])
    except Exception as e:
        print("Column data not found. \n{}".format(e))

    plt.title("{} General Graph".format(column))
    plt.savefig('graphs/general_overview_column/{}_column_general_overview.png'.format(column))
    plt.clf()


def box_graph(df):
    """
    This function generates general graph
    :param df:
    """
    df.plot.box(figsize=(30, 15))
    plt.title("General Box Graph")
    plt.savefig('graphs/box_general_graph.png')


def box_graph_column(df, column):
    """
    This function generates general graph
    :param df:
    """
    try:
        df[column].plot.box(figsize=(10, 10))
        plt.title("{} Box Graph".format(column))
        plt.savefig('graphs/box/{}_box_graph.png'.format(column))
        plt.clf()
    except Exception as e:
        print(e)


def kde(df, column):
    """
    This function generates kde graph
    :param df:
    """
    df[column].plot.kde()
    plt.title("{} Kde Graph".format(column))
    plt.savefig('graphs/kde/{}_kde_graph.png'.format(column))
    plt.clf()


def seaborn_graphs_lineplot(data, x, y):
    sns.set_theme(style="darkgrid")
    graph = sns.lineplot(x=x, y=y, data=data)
    plt.savefig("graphs/sns/{}_{}.png".format(x,y))
    plt.clf()


def seaborn_graphs_catplot(data, x, y):
    sns.set_theme(style="darkgrid")
    sns.histplot(data, x=x, hue=y, linewidth=2)
    plt.savefig("graphs/sns.catplot/{}_{}.png".format(x,y))
    plt.clf()

