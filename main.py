import process_data_helper as helper
import graph_generator
import pandas as pd
import const_variables as consts
#
# helper.create_merged_file()  # creates clean csv file

data = pd.read_csv(consts.data_file_path)  # open Dataframe with combined data
helper.clear_undefined_values(data)
data.to_csv("result_after_cleaning.csv")

# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.pie_graph(data, key)
#
# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.general_overview_column(data, key)

# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.box_graph_column(data, key)


"""
What left to do:
1. Drunk vs Fatals
2. Fatals vs Weather
3. Accident Type vs Weather
4. Drunk vs State
5. Weather condition VS peds (no in vehicle)
6. State  vs Fatals
7. test test
"""

