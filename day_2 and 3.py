# -*- coding: utf-8 -*-
"""day 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fd9L9ICfx5trX8yulordLHNGvKqg5Uz9

## **STRIP**
"""

#used to delete the blank spaces start and end of the string

txt="          Hello          "
strip_text=txt.strip()
print(strip_text)

"""# **JOIN**"""

lst=["ramya","danny","ravi","priya"]
joined_str=" ".join(lst)
print(joined_str)

"""# **READING CSV FILE**"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['loan_sanction_test.csv']))
print("The data in the start ")
print(df.head())      #default it fetches the first 5 rows
print("\n")
print("The data in the end \n" )
print(df.tail(10))    #by default it returns buttom 5 rows

#df.shape  #used to find number of rows and columns in a dataframe returns in tuple format

print("Number of rows in data frame : ", df.shape[0])
print("Number of columns in data frame : ", df.shape[1])

df.rename(columns={'Loan_ID':'ID','CoapplicantIncome':'Income'},inplace=True)  #used to rename the specified columns in the original data frame
df.head()

df.drop(columns=['Property_Area'])         #used to delete multiple rows
#df.drop(['Propert_Area','Dependents'])
#df.drop('Property_Area')                  #used to delete single row

df.dtypes          #used to find the data type of each column

"""### **DAY 3**"""

idx=df.columns   #returns the column in index format methods like intersection, union, and difference with other indices or lists can be performed
print(idx)

label=df.columns.tolist()   #returns the data in a list it does not support pandas method like intersection, union, and difference
print(label)

array_column=df.columns.values   #returns the dataframe column into numpy array which can be used for numpy functions
print(array_column)

label=df.columns[0:3]
print(label)

max_value=df['ApplicantIncome'].max()
print("Maximum value of the column :", max_value)

"""### **GETTING THE ROW INDEX**"""

idx = df.index
print(idx)
label = df.index[0]
print(label)
label = df.index[-1]
print(label)
l = df.index.tolist()
print(l)

"""### **GETTING COLUMN INDEX**"""

column_index=df.columns.get_loc('ApplicantIncome')
print(column_index)

"""### **SELECTING MULTIPLE COLUMNS BY loc and iloc functions**"""

#loc[rows:columns] i.e [start range of row:end range of row,start range of column:end range of column]

loc_data=df.loc[1:3,['ID','Gender']]
print(loc_data)

"""**1) iloc--->selects the data based on indexing**


"""

iloc_data=df.iloc[:,0:1]
print(iloc_data)

"""## **UNIQUE**"""

#used to get unique data from a particular column

unique_data=df['Education'].unique()
print(unique_data)

#to get unique data from multiple columns use for loop

columns=['Gender','Education']
for col in columns:
  unique_data=df[col].unique()
  print(unique_data)

"""### **NUNIQUE**"""

nunique_data=df.nunique()
print(nunique_data)

nunique_axis=df.nunique(axis=0,dropna=True)  #it counts unique value by columns and here null values are not counted
#if dropna=False then it counts the null values
print(nunique_axis)

nunique_axis=df.nunique(axis=1)  #it counts unique value rows
print(nunique_axis)

"""### **ISNULL**"""

# ussd to check the null values in the data if there is a null value it is assigned to True else False
data_null=df['Credit_History'].isnull()
print(data_null)

"""### **Filling null values**"""

df['Gender'].fillna("Ab",inplace=True)
print(df)

#filling the missign values using method parameter
#ffill----->forward fill, filling missing values with the values before Nan
df['Credit_History'].fillna(method='ffill',inplace=True)
print(df)

#used to fill null values with values after the Nan
df['Credit_History'].fillna(method='bfill',inplace=True)
print(df)

#restricts the number of null values that are to be filled
df.fillna(method='ffill',limit=1,inplace=True)
print(df)

"""### **Filtering data based on condition**"""

filter1=df['Gender']=='Female'
filter2=df['ApplicantIncome']>5000
con=df.where(filter1&filter2,inplace=False)
print(con)

