import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
read_Data = pd.read_csv('data.csv')

# Display the DataFrame and print "shiish"
print(read_Data, "shiish")

# Display information about the DataFrame
read_Data.info()

# Display the first 5 rows of the DataFrame
read_Data.head()

# Check for any missing values in the DataFrame
read_Data.isnull().any()

# Fill missing values with the mean of each column
read_Data.fillna(read_Data.mean(), inplace=True)

# Check again for any missing values
read_Data.isnull().any()

# Calculate column means and fill missing values with them
column_means = read_Data.mean()
read_Data = read_Data.fillna(column_means)

# Display the first 20 rows of the DataFrame
print(read_Data.head(20))

# Aggregate statistics for 'Calories' and 'Pulse' columns
res = read_Data.agg({'Calories': ['mean', 'min', 'max', 'count'],
                     'Pulse': ['mean', 'min', 'max', 'count']})
print(res)

# Filter the DataFrame for rows with calories values between 500 and 1000
filter_dst_Data1 = read_Data[(read_Data['Calories'] > 500) & (read_Data['Calories'] < 1000)]
print(filter_dst_Data1)

# Filter the DataFrame for rows with calories values > 500 and pulse < 100
filter_dst_Data2 = read_Data[(read_Data['Calories'] > 500) & (read_Data['Pulse'] < 100)]
print(filter_dst_Data2)

# Create a new DataFrame without the 'Maxpulse' column
df_modified = read_Data.loc[:, read_Data.columns != 'Maxpulse']
print(df_modified)

# Delete the 'Maxpulse' column from the main DataFrame
read_Data.drop('Maxpulse', inplace=True, axis=1)
print(read_Data.dtypes)

# Convert the datatype of 'Calories' column to int
read_Data["Calories"] = read_Data["Calories"].astype(float).astype(int)
print(read_Data.dtypes)

# Create a scatter plot for the 'Duration' and 'Calories' columns
as1 = read_Data.plot.scatter(x='Duration', y='Calories')
plt.scatter(x='Duration', y='Calories')
plt.show()
print(as1)