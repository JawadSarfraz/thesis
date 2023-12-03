import pandas as pd
from sklearn.impute import KNNImputer

# Load the dataset
df = pd.read_excel('testData.xlsx')

# Exclude non-numeric columns for imputation
numeric_columns = df.select_dtypes(include=['number']).columns

# Initialize the KNN Imputer
imputer = KNNImputer(n_neighbors=3)

# Impute the missing values in numeric columns
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

# Check the imputed values in "δ18O carb" column
imputed_values = df['δ18O carb']

# Optional: Save the imputed dataset
df.to_excel('imputed_dataset.xlsx', index=False)

# Print or return the imputed values
print(imputed_values)
