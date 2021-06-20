import process_data_helper as helper
import graph_generator
import pandas as pd
import const_variables as consts

# helper.create_merged_file()  # creates clean csv file

data = pd.read_csv(consts.data_file_path)  # open Dataframe with combined data
helper.clear_undefined_values(data)
# graph_generator.bar_graph_to_file(data, 'weather', 'caseyear')  # generate graph - weather vs year
# graph_generator.average_graph_to_file(data, 'caseyear', ['fatals', 'weather'])  # caseyear vs fatals and weather
# graph_generator.bar_graph_to_file(data, 'lgt_cond', 'caseyear')  # caseyear vs fatals
# graph_generator.bar_graph_to_file(data, 'fatals', 'weather')  # caseyear vs fatals
# graph_generator.scatter_plot_graph_to_file(data, 'fatals', 'weather')  # caseyear vs fatals

#pie graphs:
# graph_generator.pie_graph(data, 'weather')
# graph_generator.pie_graph(data, 'persons')
# graph_generator.pie_graph(data, 'state')

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

