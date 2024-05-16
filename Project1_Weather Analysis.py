import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#              Reading The Data
data = pd.read_csv(r"D:\Other\1-IBM Data Analysis\(10) Data Analyst Portfolio Projects\4- Data Analysis Projects\Python Projects - Data Analytics\Project - 1\file.csv")
#print(data.head())

#               Data Cleaning

#print(data.shape)
#print(data.index) # it shows the index range
#print(data.columns)
#print(data.dtypes)
#print(data['Weather'].unique())
#print(data['Weather'].nunique()) # to get the number of unique values in data frame or column
#print(data.nunique())
#print(data['Weather'].duplicated().sum())
#print(data.info())
#print(data.isnull().sum())
#print(data.count())  # it prints the total number of non null values in the data frame such as info()
#print(data['Weather'].value_counts()) # to get the number of unique values for each value in single column
#print(data['Weather'].value_counts().idxmax()) # to get the unique value with max number of appearances


print(data['Wind Speed_km/h'].unique(), data['Wind Speed_km/h'].nunique())

# there are 3 ways to filter to get the number of repetition of  specific value in column value_counts(), data[data.Weather == 'Clear'], data.groupby('Weather').get_group('Clear')
print(data['Weather'].value_counts())
print(data[data.Weather == 'Clear'].shape)
#print(data.groupby('Weather').get_group('Clear'))

data.rename(columns={'Weather':'Weather Condition'}, inplace=True)