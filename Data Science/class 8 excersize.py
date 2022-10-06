import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = {"Gold": [64, 224, 213, 264, 1002],
        "Silver": [102, 167, 241, 295, 795],
        "Bronze": [136, 155, 263, 293, 705]}

df = pd.DataFrame(data, index = ['Canada', 'China', 'France', 'Great Britain', 'United States'])
df

