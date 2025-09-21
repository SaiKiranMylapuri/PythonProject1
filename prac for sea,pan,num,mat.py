import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
a=pd.read_csv('car_crashes.csv')

b=a["abbrev"].unique()
i=0
c={}
for ab in b:
    c[ab]=i
    i=i+1

a.info()



