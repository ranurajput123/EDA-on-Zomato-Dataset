#!/usr/bin/env python
# coding: utf-8

# Zomato Dataset Exploratory Data Analysis
# -

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# - %matplotlib inline configures Matplotlib to generate plots and display them in the notebook output cells, rather than opening a separate window or generating a separate file.

# In[4]:


# removing encodning error
df = pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.describe()


# Data Analysis :
# - Missing Values
# - Explore about the numerical variables
# - Explore about the categorical variables
# - Finding relationship between features

# In[13]:


df.shape


# In[9]:


df.isnull().sum()


# In[11]:


# another way of finding missing values ---> using list comprehension
[features for features in df.columns if df[features].isnull().sum()>0]


# In[54]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# - Due to very low number of null values ,the above graph is so.

# In[15]:


df_country = pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[16]:


df.columns


# In[18]:


final_df = pd.merge(df,df_country,on='Country Code',how='left')


# In[19]:


final_df.head(2)


# In[20]:


## To check datatypes
final_df.dtypes


# In[21]:


final_df.columns


# In[23]:


final_df.Country.value_counts()


# In[25]:


country_names = final_df.Country.value_counts().index


# In[30]:


country_val = final_df.Country.value_counts().values


# In[40]:


## Pie Chart ---> Top 3 companies that uses zomato
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# Observations :
# - Zomato max. records or transactions are from India.
# - After that USSA and then UK.

# In[41]:


final_df.columns


# In[47]:


ratings = final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[49]:


ratings


# Observations :
# - Rating Between 4.5 to 4.9 ---> Excellent
# - Rating Between 4.0 to 4.4 ---> Very Good
# - Rating Between 3.5 to 3.9 ---> Good
# - Rating Between 3.0 to 3.4 ---> Average
# - Rating Between 2.5 to 2.9 ---> Average
# - Rating Between 1.8 to 2.4 ---> Poor
# - Rating 0  ---> Not Rated

# In[53]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x='Aggregate rating',y='Rating Count',data=ratings)


# In[60]:


sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# Observations :
# - Not rated count is very high.
# - Max. number of ratings are between 2.5 to 3.4.

# In[59]:


## Count Plot
sns.countplot(x='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[62]:


ratings


# In[64]:


## Find the countries name that has given 0 rating
final_df.columns


# In[66]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[68]:


## Or we an use this code
final_df.groupby(['Aggregate rating','Country']).size().reset_index().head()


# Observations :
# - Max. number of 0 ratings are from Indian customers.

# In[69]:


## Find out which currency is used by which country
final_df.columns


# In[70]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[72]:


## which countries do have online delivaries option
final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# Observations :
# - Online deliveries are available in India and UAE.

# In[73]:


## Create a pie chart for cities distribution.
final_df.columns


# In[74]:


final_df.City.value_counts().index


# In[75]:


city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index


# In[77]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# In[79]:


## Find top 10 Cuisines
final_df.columns


# In[83]:


final_df.groupby(['Cuisines']).size().reset_index().head(10)


# In[86]:


## Table booking in different countries 
final_df.groupby(['Has Table booking','Country']).size().reset_index()


# In[87]:


final_df.groupby(['Has Table booking','Country']).size().reset_index().max()


# In[88]:


final_df.groupby(['Has Table booking','Country']).size().reset_index().min()


# In[ ]:




