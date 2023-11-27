import pandas as pd

# Path to the Excel file
file_path = 'data.xlsx'

for i in range(1):
    # Load the Excel file
    df = pd.read_excel(file_path,7)

    # print(df.iloc[:, 10].unique())

    # # Check the data type of column J
    # print(df.iloc[:, 10].dtype)


    # Convert empty strings (or any other format representing missing values) to NaN
    df.replace('', pd.NA, inplace=True)

    # Remove rows with any missing values in columns 1 to 11
    df_cleaned = df.iloc[:, 1:11-i].dropna()

    # Save the cleaned data to a new Excel file
    cleaned_file_path = 'filterData.xlsx'
    df_cleaned.to_excel(f"filterData{i}.xlsx", index=False)



    