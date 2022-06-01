#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark


# In[2]:


from pyspark.sql import SparkSession


# In[3]:


from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.types import ArrayType, DoubleType, BooleanType
from pyspark.sql.functions import col,array_contains


# In[4]:


#creating Spark session 
spark = SparkSession.builder.appName('Assesment1').getOrCreate()


# In[5]:


#to read the data file from Local disk
Transaction_df = spark.read.csv(r"F:\PysPark\Practice\1000 BT Records.csv",sep = ',',inferSchema = True, header = True)


# In[15]:


Transaction_df.show()


# In[11]:


#Task 1 
#here we have used withColumn with that we can access all the columns of the table
from pyspark.sql.functions import trim
Transaction_df = Transaction_df.withColumn('Date', trim(Transaction_df.Date))
Transaction_df = Transaction_df.withColumn('Description',trim(Transaction_df.Description))
Transaction_df = Transaction_df.withColumn('Deposits',trim(Transaction_df.Deposits))
Transaction_df =Transaction_df.withColumn('Withdrawls',trim(Transaction_df.Withdrawls))
Transaction_df =Transaction_df.withColumn('Balance',trim(Transaction_df.Balance))


# In[14]:


Transaction_df.show()


# In[23]:


#task_2 prepare reporting dataframe for all kind of decription
#checque
cheque_df =Transaction_df.filter(Transaction_df.Description == 'Cheque')
cheque_df.count()
cheque_df.show()


# In[24]:


#ATM
ATM_df =Transaction_df.filter(Transaction_df.Description == 'ATM')
ATM_df.count()
ATM_df.show()


# In[25]:


#imps transactions 

IMPS_df =Transaction_df.filter(Transaction_df.Description == 'IMPS')
IMPS_df.count()
IMPS_df.show()


# In[26]:


Purc_df =Transaction_df.filter(Transaction_df.Description == 'Purchase')
Purc_df.count()
Purc_df.show()


# In[ ]:




