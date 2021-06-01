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
    table = pd.crosstab(df[column2], df[column1], normalize='index')
    table.plot(kind='bar', figsize=(10, 6))
    plt.title("{} vs. {}".format(column1, column2))
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.legend(consts.columns_description[column1])
    # plt.show()
    plt.savefig('graphs/{}_vs_{}.png'.format(column1, column2))
