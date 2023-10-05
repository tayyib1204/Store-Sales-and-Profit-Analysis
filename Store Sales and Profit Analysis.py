#!/usr/bin/env python
# coding: utf-8

# # Store sales and profit analysis

# Importing necessary libraries in python

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"


# In[2]:


data = pd.read_csv(r"C:\Users\Rafi\Downloads\archive (2)\Sample - Superstore.csv", encoding = 'latin-1')


# In[20]:


print(data.head()) #getting top 5 rows


# In[21]:


data.columns  #getting columns names of the dataset


# Let's look at the descriptive statistics of the dataset

# In[5]:


data.describe()


# In[6]:


print(data.isnull().values)  #finding the null values


# In[ ]:





# In the dataset we separate order date column to date, month and year to analyze each sales and profit

# In[7]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order day of week'] = data['Order Date'].dt.dayofweek


# In[8]:


data.head()


# Noe let's have a look at monthly sales

# In[9]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
fig = px.line(sales_by_month,
             x = 'Order Month',
             y = 'Sales',
             title = 'Monthly Sales Analysis')

fig.show()


# In[10]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()
fig = px.pie(sales_by_category,
            values='Sales',
            names='Category',
            hole=0.5)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))
fig.show()


# In[11]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
fig = px.bar(sales_by_subcategory,
            x = 'Sub-Category',
            y = 'Sales',
            title = 'Sales Analysis by Sub-Category')

fig.show()


# # Let's find monthly profit

# In[12]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
fig = px.line(profit_by_month,
             x = 'Order Month',
             y = 'Profit',
             title = 'Monthly Profit Analysis')
fig.show()


# # Let's find profit by category

# In[13]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()

fig = px.pie(profit_by_category,
            values = 'Profit',
            names = 'Category',
            hole=0.5)
fig.update_traces(textposition = 'inside', textinfo='percent+label')
fig.update_layout(title_text = 'Profit Analysis by Category', title_font = dict(size=24))
fig.show()


# # Now let's have a look at profit analysis by sub-category

# In[15]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory,
            x = 'Sub-Category',
            y = 'Profit',
            title = 'Profit Analysis by Sub-Category')
fig.show()


# In[18]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
color_palette = colors.qualitative.Pastel

fig = go.Figure()

fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                    y = sales_profit_by_segment['Sales'],
                    name = 'Sales',
                    marker_color = color_palette[0]))
fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                    y = sales_profit_by_segment['Profit'],
                    name = 'Profit',
                    marker_color = color_palette[1]))
fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                 xaxis_title='Customer Segment', yaxis_title='Amount')
fig.show()


# So the store has higher profits from the product sales for consumers, but the profit from corporate product sales is better in the sales-to-profit ratio. Let’s have a look at it to validate our findings

# In[19]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment', 'Sales_to_Profit_Ratio']])


# # Summary

# Store sales and profit analysis help businesses identify areas for improvement and make data-driven decisions to optimize their operations, pricing, marketing, and inventory management strategies to drive revenue and growth
