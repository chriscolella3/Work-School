import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = {'State': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
       'year': [2000, 2001, 2002, 2001, 2002, 2003],
       'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame

data = {"Gold": [64, 224, 213, 264, 1002],
        "Silver": [102, 167, 241, 295, 795],
        "Bronze": [136, 155, 263, 293, 705]}

df = pd.DataFrame(data, index = ['Canada', 'China', 'France', 'Great Britain', 'United States'])
df