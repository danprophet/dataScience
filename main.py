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

# graph_generator.general_overview_column(data, 'weather')
# graph_generator.general_overview_column(data, 'month')
graph_generator.general_overview_column(data, 'day_week')
# graph_generator.general_overview_column(data, 'hour')
# graph_generator.general_overview_column(data, 'fatals')
# graph_generator.general_overview_column(data, 'drunk_dr')
# graph_generator.general_overview_column(data, 'lgt_cond')
# graph_generator.general_overview_column(data, 'typ_int')
# graph_generator.general_overview_column(data, 'reljct1')
# graph_generator.general_overview_column(data, 'reljct2')
# graph_generator.general_overview_column(data, 'man_coll')
# graph_generator.general_overview_column(data, 'harm_ev')
# graph_generator.general_overview_column(data, 'state')


# graph_generator.general_overview_column(data, 'day_week')
# graph_generator.general_overview_column(data, 'state')
#
# for key in consts.columns_description.keys():  # this code generates all pie graphs
#     graph_generator.box_graph_column(data, key)



# graph_generator.box_graph_column(data, 'day_week')

# print(data['day_week'].value_counts(sort=False))
# graph_generator.pie_graph(data, 'day_week')

# graph_generator.bar_graph_to_file(data, 'weather', 'caseyear')  # generate graph - weather vs year
# graph_generator.average_graph_to_file(data, 'caseyear', ['fatals', 'weather'])  # caseyear vs fatals and weather
# graph_generator.bar_graph_to_file(data, 'lgt_cond', 'caseyear')  # caseyear vs fatals
# graph_generator.bar_graph_to_file(data, 'fatals', 'weather')  # caseyear vs fatals
# graph_generator.scatter_plot_graph_to_file(data, 'fatals', 'weather')  # caseyear vs fatals


# graph_generator.scatter_plot_graph_to_file(data, 'drunk_dr', 'man_coll')
# graph_generator.general_overview(data, 'Dataframe')
# graph_generator.general_overview_column(data, 'lgt_cond')
# graph_generator.graphYearVsCount(data)
# graph_generator.box_graph(data)
# graph_generator.box_graph_column(data, 'drunk_dr')
graph_generator.test(data, 'drunk_dr')

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

