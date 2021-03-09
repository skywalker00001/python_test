import pandas as pd

df = pd.read_csv('fortune500.csv')
print(df)

df.head()
df.tail()

df.columns = ['year', 'rank', 'company', 'revenue', 'profit']

df.head()

#df.dtypes

non_numberic_profits = df.profit.str.contains('[^0-9.-]')
print(non_numberic_profits)

df.loc[non_numberic_profits].head()
# df.profit[non_numberic_profits].head()

len(df.profit)

'''
#testing
import re
s = 'hello World!'

regex = re.compile("hello world!", re.I)
print (regex.match(s).group(0))
'''

set(df.profit[non_numberic_profits])

#bin_size, _, _ = plt.hist(df.year[non_numberic_profits], bins=range(1955, 2006))

df = df.loc[~non_numberic_profits]
df.profit = df.profit.apply(pd.to_numeric)
# df.loc[profit] = df.loc[profit].apply(pd.to_numeric)

df.dtypes

len(df)

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
# print(t1)
#print(t1['x'])
#print(t1['z'])

ac = t1.loc[['a', 'c'], :]
acc = t1.loc['a': 'c', :]
print(ac)
print(acc)

iac = t1.iloc[[2, 1], :]
iacc = t1.iloc[:, 1:2]
print(iac)
print(iacc)

# loc和iloc,[,]逗号左右代表行和列,可是是某个值,也可以是切片
# loc通过标签获取
# iloc通过下标获取,位置
# loc
az = t1.loc["a", 'z']
z = t1.loc[:, 'z']  # 可以切片
print(az)
print(z)
# 取第a行,和第c行[[],[]],取连续范围[,]
ac = t1.loc[['a', 'c'], :]
acc = t1.loc['b': 'c', :]
print(ac)
print(acc)
# iloc
iac = t1.iloc[[2, 1], :]
iacc = t1.iloc[:, 1:2]
print(iac)
print(iacc)

group_by_year = df.loc[:, ['year', 'revenue', 'profit']].groupby('year')
# print(group_by_year.head())
avgs = group_by_year.mean()

x = avgs.index
y = avgs['profit']


def plot(x, y, ax, title, y_label):
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    ax.margins(x=0, y=0)


#fig, ax = plt.subplots()
#plot(x, y, ax, 'Increase in mean Fortune 500 company profits from 1955 to 2005', 'Profit(millions)')

y2 = avgs.revenue
##plot(x, y2, ax, 'Increase in mean Fortune 500 company revenue from 1955 to 2005', 'Revenue(million)')


def plot_with_std(x, y, std, ax, title, y_label):
    ax.fill_between(x, y - std, y + std, alpha=0.2)
    # ax.set_ylabel(y_label)
    plot(x, y, ax, title, y_label)


fig, (ax1, ax2) = plt.subplots(ncols=2)
title = 'Increase in mean and std Fortune 500 company %s from 1995 to 2005'
stds1 = group_by_year.std().profit.values
stds2 = group_by_year.std().revenue.values
plot_with_std(x, y.values, stds1, ax1, title % 'profits', 'Profits(million)')
plot_with_std(x, y2.values, stds2, ax2, title % 'revenues', 'Revenue(million)')