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
    table.plot(kind='bar', figsize=(10, 6))
    plt.title("{} vs. {}".format(column1, column2))
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.legend(consts.columns_description[column1])
    # plt.show()
    plt.savefig('graphs/{}_vs_{}.png'.format(column1, column2))


def average_graph_to_file(df, base_column, columns_list):
    """
    This function generates base_column to columns_list average graph to PNG file
    :param df: given DataFrame
    :param base_column: base columns to be compared to
    :param columns_list: columns to be compared with base_column (average)
    """
    graph = df.groupby([base_column]).mean()[columns_list]
    graph.plot()
    # plt.show()
    plt.title("{} vs. {}".format(base_column, columns_list))
    plt.xlabel(base_column)
    plt.ylabel(columns_list)
    plt.legend(columns_list)
    # plt.show()
    plt.savefig('graphs/{}_vs_{}.png'.format(base_column, columns_list))


def scatter_plot_graph_to_file(df, x_column, y_column):
    """
    This function generates base_column to columns_list average graph to PNG file
    :param df: given DataFrame
    :param categorical_column: base columns to be compared to
    :param x_column: columns to be compared with base_column (average)
    :param y_column: columns to be compared with base_column (average)
    """
    a=sns.scatterplot(x=x_column, y=y_column, s=7, data=df)
    a.plot()
    # plt.show()
    plt.title("scatter plot - categorical_column {} vs. {}".format(x_column, y_column))
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    # plt.legend(categorical_column)
    # plt.show()
    plt.savefig('graphs/scatter_plot_{}_vs_{}.png'.format(x_column, y_column))


def graphYearVsCount(df):
    """
    This function generates graph of years vs cases
    :param df:
    :return:
    """
    data = {'years': [], 'count': []}
    for i in range(2010, 2020, 1):
        data['years'].append(i)
        data['count'].append(len(df[df['caseyear'] == i]))
    new_df = pd.DataFrame(data)
    new_df.plot(x='years')
    plt.title("{} vs. {}".format('years', 'count'))
    plt.ylim(0, 40000)
    # plt.show()
    plt.savefig('graphs/{}vs{}.png'.format('years', 'count'))


def pie_graph(df, column):
    """
    This function generates graph of years vs cases
    :param df:
    :return:
    """
    fig = plt.figure(figsize=(10,10))
    df[column].value_counts().plot(kind='pie')
    plt.title("{} Pie Graph".format(column))
    plt.savefig('graphs/{}_graph_pie.png'.format(column))
