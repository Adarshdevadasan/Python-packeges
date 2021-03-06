# -*- coding: utf-8 -*-
"""iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uD1IU8rzlw_1COpN_HjqymQ9XwYdDPSz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=sns.load_dataset("iris")
a.columns

sns.relplot(x="sepal_length",y="sepal_width",data=a)

sns.relplot(x="sepal_length",y="sepal_width",hue="species",data=a)

sns.relplot(x="petal_length",y="petal_width",data=a,kind="line")

sns.catplot(x="petal_width",y="petal_length",data=a)

sns.catplot(x="petal_width",y="petal_length",kind="violin",data=a)

sns.catplot(x="petal_width",y="petal_length",kind="boxen",data=a)

sns.set(style="white",color_codes=True)
a=sns.load_dataset("iris")
sns.boxplot(x="petal_width",y="petal_length",data=a)
sns.despine(offset=10,trim=True)

sns.set(style="white",color_codes=True)
a=sns.load_dataset("iris")
sns.boxplot(x="petal_width",y="petal_length",data=a)

sns.set(style="darkgrid")
a=sns.load_dataset("iris")
b=sns.PairGrid(a)
b.map(plt.scatter)

b=sns.PairGrid(a)
b.map(plt.scatter)

b=sns.FacetGrid(a,col="species")
b.map(plt.hist,"sepal_length")

b=np.random.normal(loc=5,size=100,scale=2)
sns.displot(b)

a=sns.load_dataset("planets")
a.columns

sns.relplot(x="method",y="mass",data=a)

sns.relplot(x="method",y="mass",hue="year",data=a)

sns.relplot(x="method",y="mass",data=a,kind="line")

sns.catplot(x="method",y="mass",data=a)

sns.catplot(x="method",y="mass",kind="violin",data=a)

sns.catplot(x="method",y="mass",kind="boxen",data=a)

sns.set(style="white",color_codes=True)
a=sns.load_dataset("planets")
sns.boxplot(x="method",y="mass",data=a)
sns.despine(offset=10,trim=True)

sns.set(style="white",color_codes=True)
a=sns.load_dataset("planets")
sns.boxplot(x="method",y="mass",data=a)

sns.set(style="darkgrid")
a=sns.load_dataset("planets")
b=sns.PairGrid(a)
b.map(plt.scatter)

b=sns.PairGrid(a)
b.map(plt.scatter)

b=sns.FacetGrid(a,col="year")
b.map(plt.hist,"method")

b=np.random.normal(loc=5,size=100,scale=2)
sns.displot(b)

