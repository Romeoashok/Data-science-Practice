#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


pd.__version__


# In[4]:


#create pandas series
#Labels -Index by default starts with 0

a = ['hi','hello','welcome']

s = pd.Series(a)

s


# In[5]:


#create pandas series with custom labels

a = ['hi','hello','welcome']

s = pd.Series(a,index=['a','b','c'])

s


# In[6]:


#Create a Pandas Series from a dictionary

a={'name':'ashok','university':'anna','year':4}

s = pd.Series(a)

s


# In[7]:


#Create a Pandas Series from a dictionary with specific keys

a={'name':'ashok','university':'anna','year':4}

s = pd.Series(a,index=['name','year'])

s


# In[8]:


#create a dataframe from two series

a = {'a':[1,2,3],'b':[4,5,6]}

s=pd.DataFrame(a)

s


# In[9]:


#specify the order of columns and define the index of the dataframe

a = pd.DataFrame({'ID':[1,2,3],'colour':['red','blue','green']},index=['a','b','c'])

a


# In[10]:


# create a DataFrame from a list of lists 

a=pd.DataFrame([[101,'red'],[102,'blue'],[103,'green']],columns = ['id','color'],index = ['a','b','c'])

a


# In[11]:


# create a NumPy array

import numpy as np

ar = np.random.rand(4,2)

ar


# In[12]:


# create a DataFrame from the NumPy array

a = pd.DataFrame(ar,columns = ['one','two'],index = [1,2,3,4])

a


# In[13]:


#loc attribute to return one or more specified rows- returns a series

a = {'a':[1,2,3],'b':[4,5,6]}

df = pd.DataFrame(a)

print(df)

df.loc[1]


# In[14]:


#return 0 and 1- returns a dataframe

df.loc[[0,1]]


# In[15]:


#use custom labels for dataframe

a = {'a':[1,2,3],'b':[4,5,6]}

df = pd.DataFrame(a,index = ['r1','r2','r3'])

df


# In[16]:


#Locate Named Indexes-returns series

df.loc['r1']


# In[17]:


#Locate Named Indexes-returns dataframes

df.loc[['r1','r3']]


# # Loading CSV File

# In[18]:


df = pd.read_csv('titanic_data.csv')

df


# # Analysing Data

# In[19]:


#To display first 10 rows of the DataFrame

df.head(10)


# In[20]:


#To display last 10 rows of the DataFrame

df.tail(10)


# In[21]:


#display information about the data

df.info()


# In[22]:


#display the datatype using dtype attribute

df.dtypes


# In[23]:


#display the shape of the dataframe

df.shape


# In[24]:


df.describe


# # #Cleaning Data
# 

# # Empty Cells

# # Data in Wrong Format

# # Wrong Data

# # Duplicates

# In[94]:


#Step 1: Analyse the data set for bad data.

df = pd.read_csv('titanic_data.csv')

df


# In[95]:


#Step2: Remove empty cells

#dropna() method returns a new DataFrame, it will not change the original.

new_df = df.dropna()

new_df


# In[96]:


#After new_df = df.dropna(inplace=true)   ##  it will not affect the original data

df


# In[97]:


#dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.

df.dropna(inplace=True)

df


# In[98]:


#After df.dropna(inplace=true) directly  ##  it will affect the original data

df


# In[99]:


#fillna(value,inplace = True ) replaces the empty cells with default value.

df=pd.read_csv('titanic_data.csv')

df.fillna(60,inplace=True)

df


# In[102]:


#replace empty values for one column

df=pd.read_csv('titanic_data.csv')

df['Survived'].fillna(250,inplace=True)

df


# # Mean , Median , Mode

# In[103]:


df = pd.read_csv('titanic_data.csv')

df


# In[104]:


#replace the empty cell of particular column with mean value - he sum of all values divided by number of values

m = df['Survived'].mean()

df['Survived'].fillna(m,inplace=True)

df


# In[106]:


#replace the empty cell of particular column with median value - the value in the middle, after sorting in ascending order.

df = pd.read_csv('titanic_data.csv')

m = df['Survived'].median()

df['Survived'].fillna(m,inplace=True)

df


# In[108]:


#replace the empty cell of particular column with mode - the value that appears most frequently
df=pd.read_csv('titanic_data.csv')

m = df['Survived'].mode()[0]

df['Survived'].fillna(m,inplace=True)

df


# In[110]:


#convert all cells in the 'Date' column into date

df=pd.read_csv('titanic_data.csv')

df['date'] = pd.to_datetime(df['date'])
df


# In[112]:


df.dropna(subset=['date'],inplace=True)

df


# In[113]:


#fix wrong values for a specific row

df.loc[8,'Survived']=60

df


# In[132]:


#replace wrong data for larger data sets with looping

for x in df.index:
    if df.loc[x,'Survived']>1:
        df.loc[x,'Survived']=1
df


# In[138]:


#delete wrong data for larger data sets with looping
for x in df.index:
    if df.loc[x,'Survived']>0:
        df.drop(x,inplace=True)
df


# # Removing Duplicates

# In[139]:


df = pd.read_csv('titanic_data.csv')
df


# In[140]:


#Identify duplicate rows-Returns True if a row is duplicated

df.duplicated()


# In[141]:


#count the duplicate rows
df.duplicated().sum()


# In[142]:


#Remove duplicate rows
df.drop_duplicates(inplace=True)
df


# # Data Correlations

# # Finding the relation Between the Columns

# # Ignore Non-Numeric Values

# # Varies from -1 to 1

# # Perfect corelation : 1

# # Good Corelation : -9 , 9

# # Corelation Limit : -6 , 6

# In[143]:


df.corr()


# In[144]:


df = pd.read_csv('titanic_data.csv')
df


# In[145]:


df.corr()


# In[ ]:




