import process_data_helper as helper
import graph_generator
import pandas as pd
import const_variables as consts
import machine_learning

# 1. Handle Data:
helper.download_api_files()  # download the files from the API
helper.create_merged_file()  # creates clean csv file
data = pd.read_csv(consts.data_file_path)  # open Dataframe with combined data
helper.clear_undefined_values(data)  # clean empty or unnecessary values
data.to_csv("csv_files/result_after_cleaning.csv")  # save the cleaned data to csv

# 2. Graph Generator:
# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.pie_graph(data, key)
#
# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.general_overview_column(data, key)
#
# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.box_graph_column(data, key)
#
# for key in consts.columns_description.keys():  #create seaborn graphs
#     for key2 in consts.columns_description.keys():
#         graph_generator.seaborn_graphs_lineplot(data, key, key2)
#
# for key in consts.columns_description.keys():  # Create bar graphs
#     for key2 in consts.columns_description.keys():
#         graph_generator.bar_graph_to_file(data, key, key2)
#
# for key in consts.columns_description.keys():  # Create Scatter Plots graphs
#     for key2 in consts.columns_description.keys():
#         graph_generator.scatter_plot_graph_to_file(data, key, key2)
#
# for key in consts.columns_description.keys():  #create seaborn graphs
#     graph_generator.kde(data, key)
#
# for key in consts.columns_description.keys():  #create seaborn graphs
#     for key2 in consts.columns_description.keys():
#         graph_generator.seaborn_graphs_catplot(data, key, key2)



graph_generator.bar_graph_to_file(data, 'weather', 'man_coll')


# ## 3. Machine Learning:
# # Can your predict the fatality rate according to the following data: Day, Month, State, Weather and Light Conditions?
# machine_learning.create_prediction(data, ['day','month', 'state', 'weather','lgt_cond'], 'fatals')
#
# # Can your predict the First Harmful event to happend,
# # according to the following data: Month, State, Weather and Light Conditions?
# machine_learning.create_prediction(data, ['month', 'state', 'weather','lgt_cond'], 'harm_ev')




"""
What left to do:
2. Fatals vs Weather
3. Accident Type vs Weather
4. Drunk vs State
5. Weather condition VS peds (no in vehicle)
6. State  vs Fatals
7. test test
"""

