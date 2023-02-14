#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:12:26 2023

@author: kiki
"""

"""Part 1: #Refer to the Titanic dataset
#Below are are a series of claims that you need to accept or reject based on visualizations of the data.
 For each one, copy and paste your final code, along with the visualization, and a statement rejecting 
 or accepting the claim into your Word document"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

df = pd.read_csv('Titanic.csv')

#Claim 1: More people died than survived 

sns.factorplot('Survived',data=df,kind='count') # Accept Claim 1

#Claim 2: Females were more likely to survive than males 
df_survived = df.loc[df['Survived']== 1]
sns.histplot(x='Sex',data = df_survived, hue ='Sex') #Accept the claim 2

#Claim 3: The third class passengers had the highest chance of survival 

sns.factorplot('Pclass',data=df,kind='count', hue='Survived') #Reject Claim 3

#Claim 4: Majority of the people in Titanic were older than 40 years

sns.histplot(data=df,x= 'Age') #Reject the Claim

#Claim 5: Majority of people paid more than 100$ for buying the ticket
paid_more = df.loc[df['Fare']>100]
paid_less = df.loc[df['Fare']<=100]
plt.hist(paid_more['Fare'])
plt.hist(paid_less['Fare'])
plt.xlabel('Fare')
plt.ylabel('Count')
plt.legend() # reject the Claim

#Claim 6: Females on an average paid more than males for buying the ticket

sns.boxplot(data=df,x = 'Sex', y= 'Fare') # Accept the Claim

#Claim 7: Passengers in Pclass 3 were younger on average than other classes

sns.boxplot(data = df, x='Pclass', y='Age') # Accept the Claim

#Claim 8: Passengers in the first class paid the highest fare

sns.boxplot(data=df,x = 'Pclass', y= 'Fare') # Accept the Claim

"""Part 2"""
#Download data for 4 of your favorite stocks 
#starting date: 01-01-2019
#end date: today (date you attempt the question)
#plot them on the same graph (only the column "Open" for each stock)
#Use appropriate names for x label, ylabel, and title
#Follow the following specifications
#Figure size: 10*10
#Title font: 25
#xticks and yticks fontsize: 15
#xlabel and ylabel font: 20
#Location of legend: upper left
#Fontsize of legend: 15


### Stock 1
apple_df = yf.download('AAPL', start = '2019-01-01',end = '2023-02-08')
### Stock 2
amazon_df = yf.download('AMZN', start = '2019-01-01',end = '2023-02-08')
### Stock 3
uber_df = yf.download('UBER', start = '2019-01-01',end = '2023-02-08')
### Stock 4
netflix_df = yf.download('NFLX', start = '2019-01-01',end = '2023-02-08')

plt.figure(figsize=(10,10))
plt.plot(apple_df['Open'],label='Apple stock', color='green')
plt.plot(amazon_df['Open'],label='Amazon stock', color='blue')
plt.plot(uber_df['Open'],label='Uber stock', color='red')
plt.plot(netflix_df['Open'],label='Netflix stock', color='orange')



plt.title('Stocks',fontsize=25)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Stock Price',fontsize=20)
plt.xticks(fontsize=15, rotation=45)
plt.yticks(fontsize=15)
plt.legend(loc='upper left',fontsize=15)





"""Part 3: Refer to file weights. It contains the weight (lbs) of randomly selected males from United States,
Verify whether the weights seem to be normally distributed"""
#Hint: Check if the distribution of data looks like a bell shaped curve
#check that the mean and median are equal (approximately)
#Check if the data follows the empirical rule
# Empirical rule: For a normal distribution about 68% of the data falls within one standard deviation, 
#about 95% percent within two standard deviations, and about 99.7% within three standard deviations from the mean.

df2 = pd.read_csv('weights.csv')
sns.histplot(data=df2,x='Weight',kde=True) #looks like a bell shaped curve

#Check if mean == weight
mean = df2['Weight'].mean()
median = df2['Weight'].median() #mean and median is almost equal

##Check if it follows the empirical rule
std = df2['Weight'].std()

lower_bound_1 = mean - std
upper_bound_1 = mean + std

lower_bound_2 = mean - 2 * std
upper_bound_2 = mean + 2 * std

lower_bound_3 = mean - 3 * std
upper_bound_3 = mean + 3 * std

data_within_1_std = df2[(df2['Weight'] >= lower_bound_1) & (df2['Weight'] <= upper_bound_1)].count()[0] / len(df2)
data_within_2_std = df2[(df2['Weight'] >= lower_bound_2) & (df2['Weight'] <= upper_bound_2)].count()[0] / len(df2)
data_within_3_std = df2[(df2['Weight'] >= lower_bound_3) & (df2['Weight'] <= upper_bound_3)].count()[0] / len(df2)

data_within_1_std # is 68.72%
data_within_2_std # is 95.32%
data_within_3_std # is 99.56%, fulfill empirical rule!

"""Part 4"""
###Box Plot
pokemon = pd.read_csv('pokemon_data.csv')

pokemon_melted = pd.melt(pokemon,id_vars=['Generation'],
                         value_vars=['HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed'],
                         var_name="Variable", value_name="Value")


sns.boxplot(x='Variable', y='Value', data=pokemon_melted, hue='Generation')
plt.legend(loc='upper right',title='Generation')

###Bar plot

pokemon_melted2 = pd.melt(pokemon,id_vars=['Legendary'],
                         value_vars=['HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed'],
                         var_name="Variable", value_name="Value")
sns.barplot(data = pokemon_melted2, x='Variable', y='Value', hue ='Legendary')
plt.legend(loc='upper right',title='Legendary')






