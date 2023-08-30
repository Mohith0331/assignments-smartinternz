# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MAK8CnpPHzcKLFUoyrBoWEfoFso86XCZ

Task - 1
Create a pandas dataframe (DataFrame name as 'df') with numpy random values (4 features and 4 observation)
"""

import pandas as pd
from numpy import random
x = random.randint(100, size=(4, 4))
df = pd.DataFrame(x)
df

"""Task - 2
Rename the task - 1 'df' dataframe column names to 'Random value 1', 'Random value 2', 'Random value 3' & 'Random value 4'
"""

df.rename(columns = {0:"Random Value 1",1:"Random Value 2",2:"Random Value 3",3:"Random Value 4"},inplace = True)
df

"""Task - 3
Find the descriptive statistics of the 'df' dataframe.
"""

df.describe()

"""Task - 4
Check for the null values in 'df' and find the data type of the columns.
"""

df.isnull().any()
df.info()

"""Task - 5
Display the 'Random value 2' & 'Random value 3' columns with location method and index location method.
"""

df.loc[0:3,"Random Value 2":"Random Value 3"]

df.iloc[0:4,1:3]