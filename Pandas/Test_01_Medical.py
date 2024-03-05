"""
 The kaggle Dataset: https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey/data?select=questionnaire.csv
"""

import pandas as pd


# Read our csv file
# url = 'https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey/data?select=questionnaire.csv'
df = pd.read_csv('./Pandas/questionnaire.csv')

# 1)Look at the dimensions overall
print(df.info)

# 2)Look at the dimensions
print(df.shape)

# Look at the data types of our columns
print(df.dtypes)

#We can use .describe for statistics on NUMERICAL columns
#It returns: count, mean, std, min, 25%, 50%, 75%, max
print(df.describe())

print(" COLUMN OPERATIONS ")

# There are 3 ways of selecting a column in pandas
# 1) df.column_name
print(df.WHQ500.head(5))

# 2) df["column_name"]
print(df["WHQ500"].head(5))

# 3) df.iloc[:, <column_number>] where iloc[rows,columns] in a way
print(df.iloc[:,-2].head(5))

print(" ROW OPERATIONS ")

# For rows we use the iloc/loc methods
# 1)df.iloc[1:10,:], numeric row selection
print(df.iloc[0:10].head(5))

# 2) df.loc[22, :] labeled based row selection only if you have an index
print(df.loc[-2,0:20])

# 3) logical-based row selection with statements. df[df["WHQ500"] >= 2.0]
print (df[df["WHQ500"] >= 2.0])
# Other useful statistics
print ("Sum of 20: ", df.WHQ500.head(20).sum())
print ("Mean of 20: ", df.WHQ500.head(20).mean())
print ("Median of 20: ", df.WHQ500.head(20).median())
print ("Unique of 20: ", df.WHQ500.head(20).nunique())
print ("Max of 20: ", df.WHQ500.head(20).max())
print ("Min of 20: ", df.WHQ500.head(20).min())

# Delete columns using the .drop method
# 1) df = df.drop("Column_Name", axis = 1)

df1 = df.drop("WHQ030M", axis = 1)

# 2) df = df.drop(columns = "Column_Name")

df2 = df.drop(columns= "WHQ030M")

# 3) df.drop( "Column_Name", axis = 1, inplace=True)
df2.drop("WHQ520", axis = 1, inplace = True)

# Deleting rows
# 1) Delete rows with labels 
df2 = df2.drop ([0,3,5], axis = 0)

# 2) Delete rows with .iloc. Basically selecting all but the first 5.
df2 = df2.iloc[5:,] #Means the same but don't take the first 5 rows

#Save our changes into a new .csv file, without new index lines and utfS8 format.
name = "proccessed"
df.to_csv(f"{name}.csv", index=False, encoding= 'utf8')




