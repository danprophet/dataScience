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
                                   ''],
                        'fatals': [''],  # fatals have no categories
                        'drunk_dr': [''],  # drunk drivers have no categories
                       'lgt_cond': ['daylight',
                                    'dark-not lighted',
                                    'dark-lighted',
                                    'dawn',
                                    'dust',
                                    'dark - unknown',
                                    'other'],
                       'typ_int': ['Not an Intersection',
                                   'Four-Way Intersection',
                                   'T-Intersection',
                                   'Y-Intersection',
                                   'Traffic Circle',
                                   'Roundabout',
                                   'Five Point, or More',
                                   '',
                                   '',
                                   'L-Intersection'],
                       'reljct1': ['No',
                                   'Yes',
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   'Not Reported',
                                   'Reported as Unknown'],
                       'reljct2': ['Non-Junction',
                                   'Intersection',
                                   'Intersection-Related',
                                   'Driveway Access',
                                   'Entrance/Exit Ramp Related',
                                   'Railway Grade Crossing',
                                   'Crossover-Related',
                                   'Driveway Access Related',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   'Shared-Use Path Crossing',
                                   'Acceleration/Deceleration Lane',
                                   'Through Roadway',
                                   'Other location within Interchange Area',
                                   'Entrance/Exit Ramp'],
                       'man_coll': ['The First Harmful Event was Not a Collision with a Motor Vehicle in Transport',
                                    'Front-to-Rear ',
                                    'Front-to-Front',
                                    '',
                                    '',
                                    '',
                                    'Angle',
                                    'Sideswipe - Same Direction',
                                    'Sideswipe - Opposite Direction',
                                    'Rear-to-Side',
                                    'Rear-to-Rear',
                                    'Other'],
                       'harm_ev' : ['Rollover/Overturn',  # 1
                                    'Fire/Explosion',  # 2
                                    'Immersion or Partial Immersion',  # 3
                                    '',  # 4
                                    'Immersion or Partial Immersion',  # 5
                                    'Injured In Vehicle (Non-Collision)',  # 6
                                    'Injured In Vehicle (Non-Collision)',  # 7
                                    'Pedestrian',  # 8
                                    'Pedalcyclist',  # 9
                                    'Railway Vehicle',  # 10
                                    'Live Animal',  # 11
                                    'Motor Vehicle In-Transport',  # 12
                                    '',  # 13
                                    'Parked Motor Vehicle ',  # 14
                                    'Non-Motorist on Personal Conveyance',  # 15
                                    'Thrown or Falling Object',  # 16
                                    'Boulder',  # 17
                                    'Other Object (not fixed)',  # 18
                                    'Building',  # 19
                                    'Impact Attenuator/Crash Cushion',  # 20
                                    'Bridge Pier or Support',  # 21
                                    '',  # 22
                                    'Bridge Rail (Includes parapet)',  # 23
                                    'Guardrail Face',  # 24
                                    'Concrete Traffic Barrier',  # 25
                                    'Other Traffic Barrier',  # 26
                                    '',  # 27
                                    '',  # 28
                                    '',  # 29
                                    'Utility Pole/Light Support',  # 30
                                    'Post, Pole or Other Supports',  # 31
                                    'Culvert',  # 32
                                    'Curb',  # 33
                                    'Ditch',  # 34
                                    'Embankment',  # 35
                                    '',  # 36
                                    '',  # 37
                                    'Fence',  # 38
                                    'Wall',  # 39
                                    'Fire Hydrant',  # 40
                                    'Shrubbery',  # 41
                                    'Tree (Standing Only)',  # 42
                                    'Other Fixed Object',  # 43
                                    'Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)',  # 44
                                    'Working Motor Vehicle ',  # 45
                                    'Traffic Signal Support',  # 46
                                    '',  # 47
                                    'Snow Bank',  # 48
                                    'Ridden Animal or Animal Drawn Conveyance',  # 49
                                    'Bridge Overhead Structure',  # 50
                                    'Jackknife (harmful to this vehicle)',  # 51
                                    'Guardrail End',  # 52
                                    'Mail Box',  # 53
                                    'Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another Motor Vehicle In Transport',  # 54
                                    '',  # 55
                                    '',  # 56
                                    'Cable Barrier',  # 57
                                    'Ground',  # 58
                                    'Traffic Sign Support ',  # 59
                                    '',  # 60
                                    '',  # 61
                                    '',  # 62
                                    '',  # 63
                                    '',  # 64
                                    '',  # 65
                                    '',  # 66
                                    '',  # 67
                                    '',  # 68
                                    '',  # 69
                                    '',  # 70
                                    '',  # 71
                                    'Cargo/Equipment Loss, Shift, or Damage [harmful]',  # 72
                                    'Object That Had Fallen From Motor Vehicle In-Transport',  # 73
                                    'Road Vehicle on Rails'  # 74
                                    ]}