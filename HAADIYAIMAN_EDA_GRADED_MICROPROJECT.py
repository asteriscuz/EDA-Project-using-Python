#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[2]:


d1=pd.read_excel('car_loan.xlsx', sheet_name='Sheet1')
d2=pd.read_excel('car_loan.xlsx', sheet_name='Sheet2')
df1 = pd.concat([d1, d2],axis=1)


# In[3]:


d3=pd.read_csv('age_band.csv')


# In[4]:


d1.shape


# In[5]:


d1


# In[6]:


d2


# In[7]:


df1


# In[8]:


dup=df1.loc[:,df1.columns.duplicated()]


# In[9]:


dup


# In[10]:


df3=df1.loc[:,~df1.columns.duplicated()]


# In[11]:


df3


# In[12]:


d3=pd.read_csv('age_band.csv')


# In[13]:


d3


# In[14]:


df=pd.concat([df3,d3], axis=1)


# In[15]:


df


# In[16]:


df.info()


# In[17]:


df['Unnamed: 1'].isnull().sum()


# I) i) Check for duplicate columns & remove them
# ii) If you want you can drop column/columns (Mention the reason for the same for removing or not)

# In[18]:


#drop the columns [Amount.Funded.By.Investors to bank] as at this stage, it does not seem important


# In[19]:


df.drop(['Amount.Funded.By.Investors to bank'], axis=1, inplace=True)


# In[20]:


# dropping customer ID too


# In[21]:


df.drop(['cust.ID'], axis=1, inplace=True)


# In[22]:


df


# 3. Clean the data (string cleaning)

# In[23]:


df.dtypes


# In[24]:


# all of the datatypes are seen as object, even though some variables like amount requested for loan need to be numeric


# In[25]:


df['Amount.Requested for loan']=pd.to_numeric(df['Amount.Requested for loan'], errors='coerce')


# In[26]:


df


# In[27]:


df['Family_incomeIncome']=pd.to_numeric(df['Family_incomeIncome'], errors='coerce')


# In[28]:


df.dtypes


# In[29]:


for num in df['Interest.Rate']:
    df['Interest.Rate']=df['Interest.Rate'].str.replace('#','')


# In[30]:


df


# In[31]:


df['Interest.Rate']=pd.to_numeric(df['Interest.Rate'], errors='coerce')


# In[32]:


df.dtypes


# In[33]:


df['Loan duration'].unique()


# In[34]:


df['Loan duration']=df['Loan duration'].str.replace('months','')
df['Loan duration']=df['Loan duration'].str.replace('>=','')
df['Loan duration']=df['Loan duration'].str.replace('.','')
df['Loan duration']=pd.to_numeric(df['Loan duration'], errors='coerce')


# In[35]:


df['Loan duration'].to_frame()


# In[36]:


df.dtypes


# In[37]:


df


# In[38]:


df['Employment.Length'].to_frame()


# In[39]:


df['Employment.Length'].value_counts().to_frame()


# In[40]:


df['Employment.Length']=df['Employment.Length'].str.replace('years','')
df['Employment.Length']=df['Employment.Length'].str.replace('year','')
df['Employment.Length']=df['Employment.Length'].str.replace('<','')
df['Employment.Length']=df['Employment.Length'].str.replace('-','')
df['Employment.Length']=df['Employment.Length'].str.replace("year's",'')
df['Employment.Length']=df['Employment.Length'].str.replace('+','')
df['Employment.Length']=pd.to_numeric(df['Employment.Length'], errors='coerce')


# In[41]:


df.dtypes


# In[42]:


df['Employment.Length'].value_counts().to_frame()


# In[43]:


df


# In[44]:


df=df.rename(columns={'Family_incomeIncome':'Family_Income'})


# In[45]:


df


# In[46]:


df['credit_score']=df['credit_score'].replace('!','')


# In[47]:


df['credit_score'].unique()


# In[48]:


df['credit_score']=df['credit_score'].str.replace('!','')


# In[49]:


df['credit_score'].unique()


# In[50]:


k=df['credit_score'].str.split('-', expand=True).astype(float)
k
# You must use expand=True if your strings have a non-uniform number of splits and you want None to replace the missing values.


# In[51]:


df['CreditScore']=(k[0]+k[1])*0.5
df.drop(['credit_score'], axis=1, inplace=True)


# In[52]:


df


# In[53]:


# separating cust.Id\tage-band \tDebt.To.Income.Ratio


# In[54]:


df[['cust.ID','age-band','Debt.To.Income.Ratio']]=df['cust.ID\tage-band \tDebt.To.Income.Ratio'].apply(lambda x: pd.Series(str(x).split('\t')))


# In[55]:


df.drop('cust.ID\tage-band \tDebt.To.Income.Ratio', axis=1, inplace=True)


# In[56]:


df


# In[57]:


df.dtypes


# In[58]:


df['cust.ID']=pd.to_numeric(df['cust.ID'], errors='coerce')


# In[59]:


df.dtypes


# In[60]:


df['Debt.To.Income.Ratio']=df['Debt.To.Income.Ratio'].str.replace('!','')


# In[61]:


df['Debt.To.Income.Ratio']=pd.to_numeric(df['Debt.To.Income.Ratio'], errors='coerce')


# In[62]:


df


# In[63]:


df['age-band'].unique()


# In[64]:


df['age-band']=df['age-band'].str.replace('!','')
df['age-band']=df['age-band'].str.replace('"45','45-55')


# In[65]:


df['age-band'].unique()


# In[66]:


df


# In[67]:


# dropping the column ['Unnamed: 1']


# In[68]:


df.drop(['Unnamed: 1'], axis=1, inplace=True)


# In[69]:


df


# In[70]:


df['owning a two wheeler'].unique()


# In[71]:


df['owning a two wheeler']=df['owning a two wheeler'].str.replace('noo','no')
df['owning a two wheeler']=df['owning a two wheeler'].str.replace('yes !','yes')
df['owning a two wheeler']=df['owning a two wheeler'].str.replace('!','')
df['owning a two wheeler']=df['owning a two wheeler'].str.replace('yes ','yes')


# In[72]:


df['owning a two wheeler'].unique()


# 2. Using seaborn/matplotlib give any two visuals and mention the insights.

# In[73]:


df


# In[74]:


plt.figure(figsize=(20,10))
sns.boxplot(df)


# In[75]:


# as is clear from the above visual, there are more outliers in family income data than others
# the data for amount requested for loan contains the highest outliers.


# In[76]:


sns.boxplot(y='Amount.Requested for loan', data=df)


# In[77]:


import plotly.express as pltx
import plotly.io as pio


# In[78]:


pltx.box(y=df['Amount.Requested for loan'])


# In[79]:


# as we can see from the box plot, there are large outliers in the data for amount requested for loan


# In[80]:


df


# In[81]:


sns.distplot(df['CreditScore'])


# In[82]:


# from the histogram, we can see that the data for credit scores is skewed to the right.


# 4. Check for outliers present in the data, decide whether you want to remove them or not. Justify the same

# In[83]:


plt.figure(figsize=(20,10))
sns.boxplot(df['Interest.Rate'])


# In[84]:


pltx.box(df['Interest.Rate'])


# there are some outliers in this data. However, since they are close to the upper whisker, removing them is not necessary and we can use some capping method to deal with them instead of removing them.

# In[85]:


plt.figure(figsize=(20,10))
sns.boxplot(df['Amount.Requested for loan'])


# in this data, since the outliers are very large and away from the upper whisker, they can be removed. If present in the data, they will impact the mean of the data.

# # PART - II
# How much missing data is there in the dataset? What's the impact of missing data on
# analysis and modelling?

# In[86]:


df.isnull().sum()


# In[87]:


# missing data leads to incorrect or incomplete analysis and also to errors in the analysis
# for modelling, it leads to building of incorrect models 


# Do the missing value imputation for numerical & categorical data

# In[88]:


df.dtypes


# In[89]:


df.drop(['cust.ID'], axis=1, inplace=True)


# In[90]:


num_col=df.select_dtypes(exclude='O')
num_col


# In[91]:


num_col.isnull().sum()


# In[92]:


df['Amount.Requested for loan'].fillna(df['Amount.Requested for loan'].median(),inplace=True)
df['Loan duration'].fillna(df['Loan duration'].median(),inplace=True)
df['Family_Income'].fillna(df['Family_Income'].median(),inplace=True)
df['Employment.Length'].fillna(df['Employment.Length'].median(),inplace=True)
df['Debt.To.Income.Ratio'].fillna(df['Debt.To.Income.Ratio'].median(),inplace=True)
# all data has outliers so we will use median to fill in the null values


# In[93]:


num_col.isnull().sum()


# In[94]:


cat_col=df.select_dtypes(include='O')
cat_col


# In[95]:


cat_col.isnull().sum()


# In[96]:


df['owning a two wheeler'].fillna(df['owning a two wheeler'].mode()[0],inplace=True)


# In[97]:


cat_col.isnull().sum()


# In[98]:


df.isnull().sum()


# 3. Which variables in the dataset require one-hot encoding using pd.getdummies? Treat them accordingly. What is the purpose of using one-hot encoding for these variables?

# 4. Is there a correlation between two numerical variables? Is it positive or negative?

# In[99]:


plt.scatter(y=df['Family_Income'],x=df['Interest.Rate'])


# In[ ]:




