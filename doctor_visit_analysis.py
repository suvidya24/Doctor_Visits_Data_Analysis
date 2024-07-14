#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# # 1.READ THE DATASET

# In[4]:


df = pd.read_csv("heathcare.csv")
print(df.head(15))


# # 2.Display complete information about the columns of the dataset such as Column name, Count, Data type and overall memory usage

# In[6]:


df.info()


# # 3.Find out the total number of people based on their count of illness

# In[7]:


df["illness"].value_counts()


# # 4. Visualize and analyse the maximum, minimum and medium income

# In[8]:


y = list(df.income)
plt.boxplot(y)
plt.show()


# # 5.Find out the number of days of reduced activity of male and female separately due to illness

# In[11]:


df.groupby(['gender', 'reduced']).mean()


# # 6. Visualize is there is any missing value in the dataset based on a heat map

# In[12]:


#missing values
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')


# # 7. Find out the correlation between variables in the given dataset correlation between different variables

# In[13]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# # 8. Analyse how the income of a patient affects the number of visits to the hospital

# In[19]:


#relation between income and visits
plt.figure(figsize=(5,5))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')


# # 9. Count and visualize the number of males and females affected by illness

# In[15]:


#number of male and female affected by illness
sns.histplot(df.gender,bins=2)


# # 10. Visualize the percentage of people getting govt health Insurance due to low income, due to old age and also the percentage of people having private health insurance

# In[20]:


# % of people getting govt Insurance due to low income
label=['yes','no']
Y = df[df['freepoor']=='yes']
N = df[df['freepoor']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(3,3))
plt.pie(x,labels=label)
plt.title("% of people getting govt health Insurance due to low income")
plt.show()
# % of people having private Insurance
Y = df[df['private']=='yes']
N = df[df['private']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(3,3))
plt.pie(x,labels=label)
plt.title("% of people having private health Insurance")
plt.show()
# % of people getting govt Insurance due to old age, disability or veteran status
Y = df[df['freerepat']=='yes']
N = df[df['freerepat']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(3,3))
plt.pie(x,labels=label)
plt.title("% of people getting govt Insurance due to old age, disability or veteran status")
plt.show()


# # 11. Plot a horizontal bar chart to analyze the reduced days of activity due to illness based on Gender

# In[17]:


db = df.groupby('gender')['reduced'].sum().to_frame().reset_index()
#creating the bar chart
plt.barh(db['gender'],db['reduced'],color = ['cornflowerblue','lightseagreen'])
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
#Show the plot
plt.show()


# In[ ]:




