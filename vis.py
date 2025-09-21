import pandas as pd
import seaborn as sns
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

a=pd.read_csv('nlp',sep=';',header=None,names=['text','emotions'])
uniqueemo=a['emotions'].unique()
emotionnum={}
i=0
for emo in uniqueemo:
    emotionnum[emo]=i
    i+=1
a['emotions']=a['emotions'].map(emotionnum)
a.to_csv('nlp model.csv',index=False)
sns.set_style('darkgrid')
sns.kdeplot(x='emotions',data=a,)
sns.despine()
plt.show()
print("hello")


