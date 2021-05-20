# ------------>>>>>>>> RUN THIS CODE CELL <<<<<<<<------------
# === CELL TYPE: IMPORTS AND SETUP

import time      # for testing use only
import os         # for testing use only

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline


def load_csv(file_name):
    file = pd.read_csv(file_name)
    return file

# 1.
# ------------>>>>>>>> RUN THIS CODE CELL <<<<<<<<------------
# --------  (run after implementation)
# === CODE TYPE: SELF TESTING
# Use the following code to test your implementation:
file_name = '.' + os.sep + 'data' + os.sep + 'imdb_movies.csv'
print(file_name)
# df_imdb_movies = load_csv(file_name)
###
### YOUR CODE HERE
###

# 3.a.
# ------------>>>>>>>> RUN THIS CODE CELL <<<<<<<<------------
# --------  (run after implementation)
# === CODE TYPE: ANSWER

def count_duplicatives(df, col_name=None):
    number_of_dup_rows = 0

    if col_name is None:  # in this case, identify full row duplicates
        result = df.duplicated(subset=None, keep=False)
    else:  # in this case, consider only col_name specific col
        result = df.duplicated(subset=col_name, keep=False)

    
    print(result)
    #     result.info
    #     print(result.cumsum(axis=0))
    return number_of_dup_rows
