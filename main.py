import process_data_helper as helper
import graph_generator
import pandas as pd
import const_variables as consts

# helper.create_merged_file()  # creates clean csv file

data = pd.read_csv(consts.data_file_path)  # open Dataframe with combined data
helper.clear_undefined_values(data)
graph_generator.bar_graph_to_file(data, 'weather', 'caseyear')
f

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

