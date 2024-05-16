# Import Libraries
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (12,8)

"""                      1- Reading The Data                     """
File_path = 'movies.csv'
df = pd.read_csv(File_path)
#Set display options for Pandas DataFrame
pd.set_option('display.max_rows', None)  # Set maximum rows to display
pd.set_option('display.max_columns', None)  # Set maximum columns to display
#print(df.info(),'\n',df.head(5))


"""                      2- Cleaning The Data                     """
# A- We will check datatype if there is any mistaken datatype, and we will change it

print(df.dtypes) # By checking each column if its data compatible with assigned datatype; therefore, afer checking there is no misconfigured datatype


# B- We will see if there is any missing data, and we will replace it

nan_counts = df.isnull().sum()
#print('\n',nan_counts)

# Replacing Blanks (NAN) of Objects or Strings with the most repetitive Values & Replacing Blancks (NAN) of float64, integers with mean
for col in df.columns:
    if df[col].dtypes == 'object':
        df[col].replace(np.nan,df[col].value_counts().idxmax(),inplace=True)
    elif df[col].dtypes == 'float64' or df[col].dtypes == 'int64':
        df[col].replace(np.nan, df[col].mean(axis=0),inplace=True)
    else:
        df[col].replace(np.nan, df[col].value_counts().idxmax(),inplace=True)

#print(df.isnull().sum(), '\n', "Data is clean from BLANKS !")

#print(df[['released','year']])

# Sorting the data based on Gross
sorted_Data = df.sort_values(by=['gross'], ascending=False)
#print(sorted_Data.head(10))

"""        3- Finding the best Correlation  """
# we will check budget v.s gross

sns.regplot(x='budget',y= 'gross',data=df,scatter_kws={"color":"red"},line_kws={"color":"blue"})
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel('Gross')
plt.grid()
plt.show()

# to show correlation between all numeric values only as Non-numeric gives an error

numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
correlation_matrix = numeric_df.corr(method='pearson')
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

# to show all data Numeric & Non-numeric and get the correlation

df_numerized = df

for col in df_numerized:
    if df_numerized[col].dtypes == 'object':
        df_numerized[col] = df_numerized[col].astype('category')
        df_numerized[col] = df_numerized[col].cat.codes

correlation_matrix2 = df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix2, annot=True)
plt.title('Correlation Matrix for All Numeric & Non-numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

corr_pairs = correlation_matrix2.unstack()
sorted_pairs = corr_pairs.sort_values(ascending= False)
high_corr = sorted_pairs[sorted_pairs > 0.5]

print(high_corr)

# Votes and budget have the highest correlation to gross earnings
