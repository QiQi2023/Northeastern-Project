#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:58:43 2023

@author: kiki
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('Titanic.csv')

##pair plot
sns.pairplot(df)

#Joint plot
sns.jointplot(x='Age', y='Fare', data=df)

##Histogram
sns.histplot(x='Fare',data=df)

##Bar plot
sns.histplot(x='Sex',data = df, hue='Sex')

## heat maps
sns.heatmap(df.corr())

##Box plot
sns.boxplot(x='Pclass',y='Age',data=df)

##scatter plot
sns.scatterplot(x='Age', y='Fare',hue='Sex',data=df)
