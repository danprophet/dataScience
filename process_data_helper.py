"""This file reads all data, and then cleans the drop_columns columns from all data,
Then combines all data to one file all_data_10-19.csv
"""
import pandas as pd
import const_variables as consts


def create_merged_file():
    """This function opens all csv files, cleans them from 'drop_columns' column list
    and creates new data csv file."""
    df = pd.read_csv("csv_files/Accidents_2010.csv")
    df.drop(consts.drop_columns, axis='columns', inplace=True)
    df.to_csv(consts.data_file_path)

    for i in range(9):
        df = pd.read_csv("csv_files/Accidents_201{}.csv".format(i+1))
        df.drop(consts.drop_columns, axis='columns', inplace=True)
        df.to_csv(consts.data_file_path, mode='a', header=False)

    df2 = pd.read_csv(consts.data_file_path)  # cleans unused column
    df2.drop(df2.columns[0], axis='columns', inplace=True)  # cleans unused column
    df2.to_csv(consts.data_file_path, index=False)  # cleans unused column


def clear_undefined_values(df):
    """
    :param: df - Dataframe
    This function clears rows from data frame according to consts.clean_dictionary
    """
    for key in consts.clean_dictionary:
        for clean_value in consts.clean_dictionary[key]:
            df.drop(df.index[df[key] == clean_value], inplace=True)
