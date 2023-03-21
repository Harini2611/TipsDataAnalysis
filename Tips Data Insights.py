#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Harini Rajarathinam
#Exploring Tips Data: Visualizing Patterns and Drawing Insights


# In[2]:


# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

#Analysis 1
# Create a scatter plot of total bill vs. tip, with point size representing party size
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='size', size='size', sizes=(20, 200))

# Set the title and axis labels
plt.title('Tip Amount vs. Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip Amount ($)')

# Display the plot
plt.show()


# In[3]:


#Analysis 2
#Distribution of tips by sex: plot the distribution of tips for males and females separately
sns.histplot(data=tips, x='tip', hue='sex', kde=True)


# In[6]:


#Analysis 3
#Average tip by day of week: calculate the average tip for each day of the week and plot the results
avg_tips_by_day = tips.groupby('day')['tip'].mean()
plt.bar(avg_tips_by_day.index, avg_tips_by_day.values)
plt.xlabel('Day of Week')
plt.ylabel('Average Tip Amount')


# In[7]:


#Analysis 4
#Correlation between total bill and tip amount: calculate the correlation between the total bill and tip amount columns
import numpy as np
corr = np.corrcoef(tips['total_bill'], tips['tip'])[0, 1]
print(f"Correlation between total bill and tip amount: {corr}")


# In[8]:


#Analysis 5
#Average tip by table size: calculate the average tip for tables of different sizes and plot the results
avg_tips_by_size = tips.groupby('size')['tip'].mean()
plt.bar(avg_tips_by_size.index, avg_tips_by_size.values)
plt.xlabel('Table Size')
plt.ylabel('Average Tip Amount')


# In[9]:


#Analysis 6
#Relationship between smoker status and tip amount: plot the relationship between smoker status and tip amount
sns.stripplot(data=tips, x='smoker', y='tip')

