# -*- coding: utf-8 -*-
"""Time_Series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O_MV3an0DRpFxg6iP8ZVEqtO4tknDAd7
"""

import pandas as pd
import matplotlib.pyplot as plt 

#[MR] Import combined dataset from public web repository
url = 'https://github.com/MatthewjRay/5010_Data/raw/main/Combined_CovidData_Clean.csv'
df = pd.read_csv(url, converters={'FIPS' : str})
df = pd.read_csv(url)

#[MR] Add month column into covid dataframe & percent of total population column
pd.to_datetime(df['Date'],)
df['Month'] = pd.DatetimeIndex(df['Date']).month_name().str[:3]
df['Death_Pct'] = df['Deaths'] / df['Census2019_18PlusPop'] * 100
df.head()

#[MR] Group plot data by month
grouped_death = df.groupby('Month')['Death_Pct'].mean()
grouped_vacc = df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean()

#[MR] Plot deaths as a percentage of total population over time (Aug - Sep 2021)
fig, ax = plt.subplots(figsize=(15,7)) 

df.groupby('Month')['Death_Pct'].mean().plot(ax=ax)
ax.set(xlabel="Month", ylabel="% of Total Pop Deaths")
plt.title("% of Total Pop. Deaths Over Time (Aug - Sep 2021)")

#[MR] Plot fully vaccinated 18+ as a percentage of total population over time (Aug - Sep 2021)
fig, ax = plt.subplots(figsize=(15,7)) 

df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean().plot(ax=ax)
ax.set(xlabel="Month", ylabel="% of Total Pop 18+ Vaccinated")
plt.title("% of 18+ Vaccinated Over Time (Aug - Sep 2021)")

##[MR] Plot fully vaccinated 18+ as a percentage of total population against deaths as a percentage of total population over time (Aug - Sep 2021)
fig, ax1 = plt.subplots(figsize=(15,7))  

ax1.set_xlabel('Date') 
ax1.tick_params(axis ='x', which='major', labelcolor = 'black')
ax1.set_ylabel('% of population 18+ Vaccinated', color = 'black') 
plot_1 = df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean().plot(ax=ax1, color = "black")
ax1.tick_params(axis ='y', labelcolor = 'black') 

ax2 = ax1.twinx()
  
ax2.set_ylabel('% of Population Deaths', color = 'green') 
plot_2 = df.groupby('Month')['Death_Pct'].mean().plot(ax=ax2, color = "green")
ax2.tick_params(axis ='y', labelcolor = 'green') 

plt.title("% of 18+ Vaccinated Vs. % of Pop. Deaths Over Time (Aug - Sep 2021)")


plt.show()