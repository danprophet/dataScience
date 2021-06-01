"This file holds const values for application use"

"proccess_data.py & process_data_helper.py"
data_file_path = 'csv_files/all_data_10-19.csv'

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
                'latitudename',
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
clean_dictionary = {"latitude": [77.7777, 88.8888, 99.9999],
                "harm_ev": [91, 93, 98, 99],
                "man_coll": [98, 99],
                "reljct1": [8, 9],
                "reljct2": [98, 99],
                "typ_int": [98, 99],
                "weather": [98, 99],
                "lgt_cond": [8, 9]}  # dictionary of column names with undefined values to be cleared from the data
columns_description = {'weather': ['Clear',
                                   'Rain',
                                   'Sleet, Hail (Freezing Rain or Drizzle)',
                                   'Snow',
                                   'Fog, Smog, Smoke',
                                   'Severe Crosswinds',
                                   'Blowing Sand, Soil, Dirt',
                                   'Other',
                                   'Cloudy',
                                   'Blowing Snow',
                                   'Freezing Rain or Drizzle'],
                       'month': ['',
                                   '',
                                   '']}