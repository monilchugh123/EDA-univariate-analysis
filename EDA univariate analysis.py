#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df=pd.read_csv("D:/ISIBangalore/MS-QMScourse/Datasets/titanic/train.csv")


# In[3]:


df.head()


# # countplot

# In[4]:


#sns.countplot(df['Survived'])
df['Survived'].value_counts().plot(kind='bar')


# In[5]:


#sns.countplot(df['Pclass'])
df['Pclass'].value_counts().plot(kind='bar')


# In[6]:


#sns.countplot(df['Sex'])
df['Sex'].value_counts().plot(kind='bar')


# In[7]:


#sns.countplot(df['Embarked'])
df['Embarked'].value_counts().plot(kind='bar')


# # pie chart

# In[8]:


df['Survived'].value_counts().plot(kind='pie', autopct='%.2f')


# In[9]:


df['Pclass'].value_counts().plot(kind='pie', autopct='%.2f')


# In[10]:


df['Sex'].value_counts().plot(kind='pie', autopct='%.2f')


# In[11]:


df['Embarked'].value_counts().plot(kind='pie', autopct='%.2f')


# # Numerical data

# 1. Histogram

# In[12]:


import matplotlib.pyplot as plt


# In[13]:


plt.hist(df['Age'],bins=20)


#  2. Distplot

# In[14]:


sns.distplot(df['Age'])


# In[15]:


sns.histplot(df['Age'])


# 3.boxplot

# In[16]:


sns.boxplot(df['Age'])


# In[17]:


sns.boxplot(df['Fare'])


# In[18]:


df['Age'].min()


# In[19]:


df.describe()


# In[20]:


df.info()


# In[21]:


df['Age'].skew()


# In[22]:


df['Age'].median()


# In[ ]:





# In[ ]:




