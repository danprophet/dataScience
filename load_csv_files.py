"""This file reads all data, and then cleans the drop_columns columns from all data,
Then combines all data to one file all_data_10-19.csv
"""

import pandas as pd

drop_columns = ['st_case',
                'statename',
                've_total',
                've_forms',
                'pvh_invl',
                'pernotmvit',
                'permvit',
                'county',
                'countyname',
                'city',
                'cityname',
                'monthname',
                'day_week',
                'day_weekname',
                'hour',
                'hourname',
                'minute',
                'minutename',
                'nhs',
                'nhsname',
                'rur_urb',
                'rur_urbname',
                'func_sys',
                'func_sysname',
                'rd_owner',
                'rd_ownername',
                'route',
                'routename',
                'tway_id',
                'tway_id2',
                'milept',
                'mileptname',
                'longitud',
                'longitudname',
                'sp_jur',
                'sp_jurname',
                'harm_evname',
                'man_collname',
                'reljct1name',
                'reljct2name',
                'typ_intname',
                'wrk_zone',
                'wrk_zonename',
                'road_fnc',
                'road_fncname',
                'rel_road',
                'rel_roadname',
                'lgt_condname',
                'weather1',
                'weather1name',
                'weather2',
                'weather2name',
                'weathername',
                'sch_bus',
                'sch_busname',
                'rail',
                'railname',
                'not_hour',
                'not_hourname',
                'not_min',
                'not_minname',
                'arr_hour',
                'arr_hourname',
                'arr_min',
                'arr_minname',
                'hosp_hr',
                'hosp_hrname',
                'hosp_mn',
                'hosp_mnname',
                'cf1',
                'cf1name',
                'cf2',
                'cf2name',
                'cf3',
                'cf3name']  # list of columns to omit from the csv data retrieved with the api

df = pd.read_csv("csv_files/Accidents_2010.csv")
df.drop(drop_columns, axis='columns', inplace=True)
df.to_csv('csv_files/all_data_10-19.csv')

for i in range(8):
    df = pd.read_csv("csv_files/Accidents_201{}.csv".format(i+1))
    df.drop(drop_columns, axis='columns', inplace=True)
    df.to_csv('csv_files/all_data_10-19.csv', mode='a', header=False)
    # print(df)


df2 = pd.read_csv("csv_files/all_data_10-19.csv")
df2.drop(df2.columns[0], axis='columns', inplace=True)
df2.to_csv('csv_files/all_data_10-19.csv', index=False)
print(df2)