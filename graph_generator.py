"This python file will handle processing csv data to different graphs"

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import const_variables as consts
# %matplotlib inline  # ???


file = pd.read_csv(consts.data_file_path)
print (file)