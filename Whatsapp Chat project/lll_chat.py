# -*- coding: utf-8 -*-
"""lll_chat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z9Z_zcZgqS6roLZxmGoRclOVUpMdIP4n
"""

# Commented out IPython magic to ensure Python compatibility.
!pwd
# %ls

import pandas as pd

df1 = pd.read_excel("Final_chat.xlsx", header=None, names=['Date','Time','Author','Message'])
df1.head()

df1.isnull().values.any()
#df1.head()
df1.isnull().sum()  #to find how many null values are present

df_trial=df1.copy()
#df_trial.head()

df_trial=df_trial.drop(df_trial[df_trial.Date.isnull()].index)
df_trial.isnull().sum()

df_trial=df_trial.drop(df_trial[df_trial.Author.isnull()].index)
df_trial.isnull().sum()

#df_trial.head()
df_trial.shape

df1=df_trial.copy()
df1.shape

import numpy as np
import seaborn as sns

from sklearn.model_selection import cross_val_score

Sneha = df_trial.apply(lambda x: True if x['Author'] == 'Sneha Gathani' else False, axis = 1)
SnehaRows = len(Sneha[Sneha == True].index)
print("Number of messages by Sneha : ", SnehaRows)

Priyankaa = df_trial.apply(lambda x: True if x['Author'] == 'Priyankaa Parakh' else False, axis = 1)
PriRows = len(Priyankaa[Priyankaa == True].index)
print("Number of messages by Priyankaa : ", PriRows)

Kinjal = df_trial.apply(lambda x: True if x['Author'] == 'Kinjal Sanghvi' else False, axis = 1)
KinRows = len(Kinjal[Kinjal == True].index)
print("Number of messages by Kinjal : ", KinRows)

Kajal = df_trial.apply(lambda x: True if x['Author'] == 'Kajal Oswal' else False, axis = 1)
KajalRows = len(Kajal[Kajal == True].index)
print("Number of messages by Kajal : ", KajalRows)

Pranjal = df_trial.apply(lambda x: True if x['Author'] == 'Pranjal Malu' else False, axis = 1)
PranjalRows = len(Pranjal[Pranjal == True].index)
print("Number of messages by Pranjal : ", PranjalRows)

Parthvi = df_trial.apply(lambda x: True if x['Author'] == 'Parthvi Patel' else False, axis = 1)
ParthviRows = len(Parthvi[Parthvi == True].index)
print("Number of messages by Parthvi : ", ParthviRows)

Tanvi = df_trial.apply(lambda x: True if x['Author'] == 'Tanvi Mehta' else False, axis = 1)
TanviRows = len(Tanvi[Tanvi == True].index)
print("Number of messages by Tanvi : ", TanviRows)

data = {'Author': ['Sneha Gathani', 'Priyankaa Parakh', 'Kinjal Sanghvi', 'Kajal Oswal', 'Pranjal Malu', 'Parthvi Patel', 'Tanvi Mehta'], 'MessageCount':[SnehaRows,PriRows,KinRows,KajalRows,PranjalRows, ParthviRows,TanviRows]}

df_count = pd.DataFrame(data)
df_count

df_count.MessageCount.mean()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

df_trial.describe()

author_value_counts = df_trial['Author'].value_counts() # Number of messages per author
top_7_author_value_counts = author_value_counts.head(7) # Number of messages per author for the top 10 most active authors
top_7_author_value_counts.plot.barh() # Plot a bar chart using pandas built-in plotting apis
plt.xlabel('Number of Messages')
plt.ylabel('Author')

media_messages_df = df_trial[df_trial['Message'] == '<Media omitted>']
#print(media_messages_df.head())

author_media_messages_value_counts = media_messages_df['Author'].value_counts()
top_7_author_media_messages_value_counts = author_media_messages_value_counts.head(10)
top_7_author_media_messages_value_counts.plot.barh()
plt.xlabel('Number of Medias')
plt.ylabel('Author')

df_trial['Date'].value_counts().head(10).plot.barh() # Top 10 Dates on which the most number of messages were sent
plt.xlabel('Number of Messages')
plt.ylabel('Date')

df_trial['Time'].value_counts().head(10).plot.barh() # Top 10 Times of the day at which the most number of messages were sent
plt.xlabel('Number of messages')
plt.ylabel('Time')

#df_trial.head(10)
df_filtered = df_trial.copy();
#df_trial.head(10)

indexNames = df_filtered[ (df_filtered['Author'] != 'Sneha Gathani') & (df_filtered['Author'] != 'Priyankaa Parakh')& (df_filtered['Author'] != 'Kinjal Sanghvi')& (df_filtered['Author'] != 'Parthvi Patel')& (df_filtered['Author'] != 'Pranjal Malu')& (df_filtered['Author'] != 'Tanvi Mehta')& (df_filtered['Author'] != 'Kajal Oswal') ].index
df_filtered.drop(indexNames , inplace=True)
df_filtered.head(10)

df_trial = df_trial.query("Author in ['Sneha Gathani', 'Priyankaa Parakh']")
#df_trial.head(10)
df_trial.describe()