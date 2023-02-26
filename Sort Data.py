#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:12:17 2023

@author: kiki
"""

#Import the data and relevant libraries
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df= pd.read_excel('alcohol.xlsx')

#sort data based on decreasing beer_servings and assign it to a variable called sort_beer

sort_beer = df.sort_values('beer_servings', ascending= False)

#which country drinks the highest spirit_servings
 
df[df.spirit_servings == df.spirit_servings.max()].country

#get all rows with beer servings greater than 100

df.loc[df['beer_servings'] > 100]

#get all rows with beer servings greater than 100 in Asia (AS)

df.loc[(df['beer_servings'] > 100) & (df['continent'] == 'AS')]

#get all the rows for continent "A"

df.loc[df['continent'] == 'A']

#get the mean alcohol consumption per continent for every column (hint: use groupby)

df.groupby('continent').mean()

#get the median alcohol consumption per continent for every column

df.groupby('continent').median()

#Create a new column called total_servings which is the sum of beer_servings, spirit_servings, wine_servings

df['total_servings'] = df['beer_servings'] + df['spirit_servings'] + df['wine_servings']

#Sort the data based on total_servings and state which country drinks most and which drinks least

df.sort_values('total_servings', ascending = False)
'''
The country drinks the most is Andorra, the total servings is 695.
There are multiple country drinks the least, total servings of these countries are all 0:
    Libya, Mauritania, Somalia, Afghanistan, Bangladesh, North Korea,Iran,
    Kuwait, Maldives, Pakistan, Monaco, San Marino, Marshall Islands

'''

#Read column beer_servings

df['beer_servings']

#Read columns beer_servings and wine_servings

df[['beer_servings', 'wine_servings']]

#for countries that drink more than 200 servings of beer, change their (country names) names to "beer nation"

df.loc[df['beer_servings']>200, ['country']]='beer nation' 

#save the data frame as an Excel file with name updated_drinks_excel

df.to_excel('updated_drinks.xlsx')

#save the data frame as a csv file with name updated_drinks_csv

df.to_csv('updated_drinks.csv')

#Write a program to print the cube of numbers from 2 to 100 (including both 2 and 100)

list_cube=[]

for i in range(2,101):
    list_cube.append(i**3)
    print(list_cube)

#Write a program to print the cube of even numbers from 2 to 100 (including both 2 and 100)

list_cube_even = []
for i in range(2,101):
    cube = i**3
    if cube % 2 == 0:
        list_cube_even.append(cube)
        print(list_cube_even)

#Give 5 examples of reserved words in python

'''
As, is, in, def, else, if
'''

#give 4 examples of bad variable names and state why they are invalid

'''
Examples: iaejfnlaknb394, cra, #sing, var.4
Bad varibale names are invalid since they don't have any meaning, it cause
difficulties in reading. They are too abstract which makes the code hard to read.

'''


