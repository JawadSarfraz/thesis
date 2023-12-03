import pandas as pd

# Path to the Excel file
file_path = 'data.xlsx'

df = pd.read_excel(file_path,4)

# print(df.iloc[:, 10].unique())

# # Check the data type of column J
# print(df.iloc[:, 10].dtype)
df.replace('', pd.NA, inplace=True)

# Exclude columns
columns_to_exclude = [10]
df_modified = df.drop(df.columns[columns_to_exclude], axis=1)

df_modified.iloc[:, 9] = df_modified.iloc[:, 9].round(2)

# Remove rows with any missing values in the remaining columns
df_cleaned = df_modified.iloc[:, 0:11].dropna()

# Save the cleaned data to a new Excel file
cleaned_file_path = 'resultFile_1.xlsx'
df_cleaned.to_excel(cleaned_file_path, index=False)