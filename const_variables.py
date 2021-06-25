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
                'day_weekname',
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
                "lgt_cond": [8, 9],
                "hour": [99]}  # dictionary of column names with undefined values to be cleared from the data
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
                       'month': ['January',
                                 'February',
                                 'March',
                                 'April',
                                 'May',
                                 'June',
                                 'July',
                                 'August',
                                 'September',
                                 'October',
                                 'November',
                                 'December'],
                       'caseyear': [ '2010',
                                 '2011',
                                 '2012',
                                 '2013',
                                 '2014',
                                 '2015',
                                 '2016',
                                 '2017',
                                 '2018',
                                 '2019'],
                       'day_week': ['Sunday',
                                    'Monday',
                                    'Tuesday',
                                    'Wednesday',
                                    'Thursday',
                                    'Friday',
                                    'Saturday'],
                       'hour': ['0',
                                '1',
                                '2',
                                '3',
                                '4',
                                '5',
                                '6',
                                '7',
                                '8',
                                '9',
                                '10',
                                '11',
                                '12',
                                '13',
                                '14',
                                '15',
                                '16',
                                '17',
                                '18',
                                '19',
                                '20',
                                '21',
                                '22',
                                '23'],
                        'fatals': ['0',
                                   '1',
                                   '2',
                                   '3',
                                   '4',
                                   '5',
                                   '6',
                                   '7',
                                   '8',
                                   '9',
                                   '10',
                                   '11',
                                   '12',
                                   '13',
                                   '14',
                                   '15',
                                   '16',
                                   '17',
                                   '18',
                                   '19',
                                   '20'],  # Fatals have no categories
                        'drunk_dr': ['0',
                                     '1',
                                     '2',
                                     '3',
                                     '4',],  # Drunk drivers have no categories
                       'lgt_cond': ['daylight',
                                    'dark-not lighted',
                                    'dark-lighted',
                                    'dawn',
                                    'dust',
                                    'dark - unknown',
                                    'other'],  # Light Condition
                       'typ_int': ['Not an Intersection',
                                   'Four-Way Intersection',
                                   'T-Intersection',
                                   'Y-Intersection',
                                   'Traffic Circle',
                                   'Roundabout',
                                   'Five Point, or More',
                                   '',
                                   '',
                                   'L-Intersection'],  # Type of Intersection
                       'reljct1': ['No',
                                   'Yes',
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   '',  # not relevant
                                   'Not Reported',
                                   'Reported as Unknown'],  # Relation to Junction- Within Interchange Area
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
                                   'Entrance/Exit Ramp'],  # Relation to Junction- Specific Location
                       'man_coll': ['The First Harmful Event was Not a Collision with a Motor Vehicle in Transport',
                                    'Front-to-Rear ',
                                    'Front-to-Front',
                                    'Angle – Front-to-Side, Same Direction',
                                    'Angle – Front-to-Side, Opposite Direction',
                                    'Angle – Front-to-Side, Right Angle (Includes Broadside)',
                                    'Angle – Front-to-Side/Angle-Direction Not Specified',
                                    'Sideswipe - Same Direction',
                                    'Sideswipe - Opposite Direction',
                                    'Rear-to-Side',
                                    'Rear-to-Rear',
                                    'Other'],  # Manner of Collision of the First Harmful Event
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
                                    ],  # First Harmful Event
                       'state': ['Alabama ',  # 1
                                 'Alaska ',  # 2
                                 'Arizona ',  # 4
                                 'Arkansas ',  # 5
                                 'California ',  # 6
                                 'Colorado ',  # 8
                                 'Connecticut ',  # 9
                                 'Delaware ',  # 10
                                 'District of Columbia ',  # 11
                                 'Florida ',  # 12
                                 'Georgia ',  # 13
                                 'Hawaii ',  # 15
                                 'Idaho ',  # 16
                                 'Illinois ',  # 17
                                 'Indiana ',  # 18
                                 'Iowa ',  # 19
                                 'Kansas ',  # 20
                                 'Kentucky ',  # 21
                                 'Louisiana ',  # 22
                                 'Maine ',  # 23
                                 'Maryland ',  # 24
                                 'Massachusetts ',  # 25
                                 'Michigan ',  # 26
                                 'Minnesota ',  # 27
                                 'Mississippi ',  # 28
                                 'Missouri ',  # 29
                                 'Montana',  # 30
                                 'Nebraska',  # 31
                                 'Nevada',  # 32
                                 'New Hampshire',  # 33
                                 'New Jersey',  # 34
                                 'New Mexico',  # 35
                                 'New York',  # 36
                                 'North Carolina',  # 37
                                 'North Dakota',  # 38
                                 'Ohio',  # 39
                                 'Oklahoma',  # 40
                                 'Oregon',  # 41
                                 'Pennsylvania',  # 42
                                 'Puerto Rico',  # 43
                                 'Rhode Island',  # 44
                                 'South Carolina',  # 45
                                 'South Dakota',  # 46
                                 'Tennessee',  # 47
                                 'Texas',  # 48
                                 'Utah',  # 49
                                 'Vermont',  # 50
                                 'Virginia',  # 51
                                 'Virgin Islands ',  # 52
                                 'Washington',  # 53
                                 'West Virginia',  # 54
                                 'Wisconsin',  # 55
                                 'Wyoming'],
                       'columns': {'caseyear': 'Years',
                                   'state': 'State Number',
                                   'peds': 'Number of Forms Submitted for Persons Not in Motor Vehicles',
                                   'persons': 'Number of Forms Submitted for Persons in Motor Vehicles',
                                   'day': 'Days',
                                   'month': 'Months',
                                   'year': 'Years',
                                   'day_week': 'Days',
                                   'hour': 'Hours',
                                   'latitude': 'Latitude Coordinate',
                                   'longitud': 'Longitude Coordinate',
                                   'harm_ev': 'First Harmful Event',
                                   'man_coll': 'Manner of Collision of the First Harmful Event',
                                   'reljct1': 'Relation to Junction- Within Interchange Area',
                                   'reljct2': 'Relation to Junction- Specific Location',
                                   'typ_int': 'Type of Intersection',
                                   'lgt_cond': 'Light Condition',
                                   'weather': 'Weather',
                                   'fatals': 'Fatals',
                                   'drunk_dr': 'Number of Drinking Drivers'}}  # States

