import pandas as pd
import numpy as np


# 🐍🐍🐍🐍 Pandas Series: A Pandas Series is like a column in a table.

# a = [1,2,3]
# pd_series = pd.Series(a) # By default index start from 0.
# pd_series = pd.Series(a, index=["x","y","z"]) # With the index argument, you can name your own indexes.
# print(pd_series)


# 🐍🐍🐍🐍 Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"]) # To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
# print(myvar)



# 🐍🐍🐍🐍 What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


# if this is dataframe of stock market

# data = {
#     "Symbol": ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT"],
#     "Open": [175.5, 2800.0, 650.5, 3500.2, 320.8],
#     "High": [180.2, 2850.5, 670.0, 3550.7, 325.3],
#     "Low": [172.1, 2785.8, 640.3, 3480.5, 315.2],
#     "Close": [178.5, 2825.3, 660.2, 3520.4, 322.7],
#     "Volume": [120000, 85000, 150000, 65000, 98000],
#     "EntryTime": pd.to_datetime(["2025-03-01 09:30:00", "2025-03-02 10:00:00", "2025-03-03 09:45:00", "2025-03-04 11:15:00", "2025-03-05 10:30:00"]),
#     "ExitTime": pd.to_datetime(["2025-03-01 15:30:00", "2025-03-02 16:00:00", "2025-03-03 14:45:00", "2025-03-04 15:15:00", "2025-03-05 15:30:00"]),
#     "Quantity": [100, 50, 75, 40, 60],
#     "EntryPrice": [176.0, 2810.0, 655.0, 3510.0, 321.0],
#     "ExitPrice": [178.5, 2825.3, 660.2, 3520.4, 322.7],
#     "Position": ["Long", "Short", "Long", "Short", "Long"]
# }

# df = pd.DataFrame(data)
# df = pd.DataFrame(data, index=["day1","day2","day3", "day4", "day5"]) # You can add index in df
# print(df.loc["day2"])
# print(df.loc[[0,1,2]]) # get the specific rows data if index not defined

# df["PnL"] = np.where(df["Position"] == "Long",
#                      (df["ExitPrice"] - df["EntryPrice"]) * df["Quantity"],
#                      (df["EntryPrice"] - df["ExitPrice"]) * df["Quantity"])
# print(df)

# 🐍🐍🐍🐍 read the df from csv
# df = pd.read_csv("data.csv")
# print(df.to_string()) # use to_string() to print the entire DataFrame.

# 🐍🐍🐍🐍 read the df from json
# df = pd.read_json('data.json')
# print(df) # print some starting and ending lines
# print(df.to_string()) # print complete json

# 🐍🐍🐍🐍 display max rows
# print(pd.options.display.max_rows)  # by default it is 60 (i think)
# pd.options.display.max_rows = 9999 # you can give the value (means how many max rows you want) also
# df = pd.read_csv("data.csv")
# print(df.to_string())


# 🐍🐍🐍🐍 head method
# The head() method returns the headers and a specified number of rows, starting from the top.

# df = pd.read_csv("data.csv")
# print(df.head()) # if number of rows not specified then it gives you top 5 rows from csv or json
# print(df.head(10)) # gives you top 10 rows


# 🐍🐍🐍🐍 tail method
# The tail() method returns the headers and a specified number of rows, starting from the bottom.

# df = pd.read_csv("data.csv")
# print(df.tail()) # if number of rows not specified then it gives you bottom 5 rows from csv or json
# print(df.tail(10)) # gives you top 10 rows







# 🐍🐍🐍🐍 CLEANING DATAFRAMES: Data cleaning means fixing bad data in your data set. like 

# 1. Empty cells
# 2. Data in wrong format
# 3. Wrong data
# 4. Duplicates
# 5. In this tutorial you will learn how to deal with all of them.


# 🐍🐍🐍🐍 1. Cleaning Empty Cells
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# df = pd.read_csv('empty_cells.csv')
# new_df = df.dropna()
# print(new_df.to_string())


# 🐍🐍🐍🐍 If you want to change the original DataFrame, use the inplace = True argument:
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# df = pd.read_csv('empty_cells.csv')
# df.dropna(inplace = True) # Remove all rows with NULL values 
# print(df.to_string())


# 🐍🐍🐍🐍 The fillna() method allows us to replace empty cells with a value::

# df = pd.read_csv('fillna_cells.csv')
# df.fillna(00, inplace = True) # You can give specific column there
# df["Calories"].fillna(000, inplace = True) # for some specified columnn
# print(df.to_string())


# 🐍🐍🐍🐍 To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# df = pd.read_csv('wrong_format.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# # df.dropna(subset=['Date'], inplace = True) # Remove rows with a NULL value in the "Date" column:
# print(df.to_string()) # not print something wrong here


# 🐍🐍🐍🐍 Fixing Wrong Data

# df = pd.read_csv('wrong_data.csv')

# for x in df.index:
#   if df.loc[x, "Duration"] > 120: # type: ignore
#     df.loc[x, "Duration"] = 120

# print(df.to_string())


# 🐍🐍🐍🐍 Removing Duplicates: To remove duplicates, use the drop_duplicates() method.
# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

# df = pd.read_csv('duplicate.csv')
# # print(df.duplicated()) # Returns True for every row that is a duplicate, otherwise False:
# df.drop_duplicates(inplace=True)
# print(df)