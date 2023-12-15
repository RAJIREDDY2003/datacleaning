import pandas as pd
# Load your existing dataset (replace 'your_dataset.csv' with your actual file)
file_path = 'dataset.csv'
df = pd.read_csv(file_path)

# Display the summary statistics of the dataset
print("Before Cleaning:")
print(df.describe())

# Replace missing values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Remove outliers based on z-scores for numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
z_scores = (df[numeric_columns] - df[numeric_columns].mean()) / df[numeric_columns].std()
df = df[(z_scores.abs() < 3).all(axis=1)]

# Save the cleaned dataset to a new CSV file
cleaned_file_path = 'cleaned_dataset.csv'
df.to_csv(cleaned_file_path, index=False)

# Display the summary statistics of the cleaned dataset
print("\nAfter Cleaning:")
print(df.describe())

print(f"\nCleaned dataset saved to {cleaned_file_path}.")
    
