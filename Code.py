import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('RGA.csv')

# Transpose the DataFrame, including column names
df_transposed = df.transpose().reset_index()

# Set the first row as the new column names
df_transposed.columns = df_transposed.iloc[0]

# Drop the first row, which contains the original column names
df_transposed = df_transposed[1:]

# Save the transposed data to a new CSV file
df_transposed.to_csv('output.csv', index=False)
