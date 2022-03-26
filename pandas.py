# -*- coding: utf-8 -*-
"""pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dYZu9onTy66dk7ZPOzHz9FPABOoiOmx9
"""

# dataframe

import pandas as pd
import numpy as np
from numpy.random import randn

df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='w x y z'.split())
df

# pass a list of cloumn names
df[['w','z']]

type(df['w'])

# **creating a new cloumn:**
df['new']=df['w']+df['y']
df

# **Removing columns**
df.drop('new',axis=1)

df.drop('E',axis=0)

# Selecting rows
df.loc['A']

# Or select based off position instead of label
df.iloc[2]

# selecting subset of rows and cloumns
df.loc['B','y']

df.loc[['A','B'],['w','y']]

## conditional selection
# An important feature of pandas is condtional selection using bracket notation, very similar to numpy:

df

df>0

df[df>0]

df[df['w']>0]

df[df['w']>0]['y']

df[df['w']>0][['y','x']]

# For two conditions you can use and & with paranthesis:
df[df['w']>0&(df['y']>1)]

df

# reset to default 0,1...n index
df.reset_index()

newind='CA NY WY OR CO'.split()
df['states']=newind
df

df.set_index('states',inplace=True)
df

# Multi-Index and Index Hierarchy
# Index levels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
hier_index

df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df

df.loc['G1']

df.loc['G1'].loc[1]

df.index.names

df.index.names=['Group','Num']
df

# xs function return the specified portion from the dataframe
# here the function returns the value from the index 'G1
df.xs('G1')

df.xs(['G1',1])

df.xs(1,level='Num')

# SERIES

## creating a series
# you can convert a list,numpy array,or dictionary to a series:
labels=['a','b','c']
my_list=[10,20,30]
arr=np.array([10,20,30])
d={'a':10,'b':20,'c':30}

# **Using Lists**

pd.Series(data=my_list)

pd.Series(data=my_list,index=labels)

pd.Series(my_list,labels)

pd.Series(arr)

pd.Series(arr,labels)

# **Dictionary**
pd.Series(d)

# data in aseries
# A pandas series can hold a variety of objects types:
pd.Series(data=labels)

## using an index
ser1=pd.Series([1,2,3,4],index=['USA','Germany','USSR','Japan'])
ser1

ser2=pd.Series([1,2,5,4],index=['USA','Germany','Italy','Japan'])
ser2

ser1['USA']

# Operations are them also done based off of index:
ser1+ser2

# Missing DATA
df=pd.DataFrame({'A':[1,2,np.nan],
                 'B':[5,np.nan,np.nan],
                 'C':[1,2,3]})
df

df.dropna()

df.dropna(axis=1)

# thresh takes integer value which tells minimum amount of na values to drop.
df.dropna(thresh=2)

df.fillna(value='FILL VALUE')

df['A'].fillna(value=df['A'].mean())

# GROUP BY
# Create dataframe
data={'company':['GOOG','GOOG','MSFT','MSFT','FB','FB',],
      'person':['sam','charlie','amy','vanessa','carl','sarah'],
      'sales':[200,120,340,124,243,350]}
df=pd.DataFrame(data)
df

df.groupby('company')

# You can save the object as a new variables:
by_comp=df.groupby("company")

by_comp

by_comp.mean()

df.groupby('company').mean()

# More examples of aggragate methods:
by_comp.std()

by_comp.min()

by_comp.max()

by_comp.count()

by_comp.describe()

by_comp.describe().transpose()

by_comp.describe().transpose()['GOOG']

# OPERATIONS
df=pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head

df['col2'].unique()

# pandas nunique() is used to get a count of unique values.
df['col2'].nunique()

df['col2'].value_counts()

# select from dataframe using criteria from multiple columns
newdf=df[(df['col1']>2)&(df['col2']==444)]
newdf

df['col3'].apply(len)

df['col3'].apply(len)

df['col1'].sum()

# Permanently Removing a column
del df['col1']
df

df.columns

df.index

df

df.sort_values(by='col2')#insplace=false by default

## find null values or check for null values
df.isnull()

# drop rows with nan values
df.dropna()

df=pd.DataFrame({'coll':[1,2,3,np.nan],
                 'col2':[np.nan,555,666,444],
                 'col3':['abc','def','ghi','xyz']})
df.head()

df.fillna('FILL')

data={'A':['foo','foo','foo','bar','bar','bar'],
      'B':['one','one','two','two','one','one'],
      'C':['x','y','x','y','x','y'],
      'D':[1,3,2,5,4,1]}
df=pd.DataFrame(data)

df