import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv('Baltimore.csv')

#Remove dollar signs in Annual Salary column and assign it as float 
df['AnnualSalary'] = df['AnnualSalary'].astype(str)
df['AnnualSalary'] = df['AnnualSalary'].apply(lambda x: x.replace('$',''))
df['AnnualSalary'] = df['AnnualSalary'].astype(float)

#Group the data and aggregate with sum,mean
group = df.groupby(['JobTitle'])['AnnualSalary']
aggregate = group.agg([np.sum,np.mean])
print(aggregate)

#How many employees for each job roles
df['JobTitle'].value_counts()[0:10].plot(kind = 'bar')

#List of all the Agency ID and Agency Name
id_name = df[['Agency','AgencyID']]
id_name.drop_duplicates(inplace=True)
print(id_name)

#To find all the missing Gross data in dataset
df['GrossPay'].isnull().sum()