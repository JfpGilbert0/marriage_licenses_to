#### Preamble ####
# Purpose: Cleans the raw plane data recorded by two observers..... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 6 April 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]

#### Workspace setup ####
import pandas as pd


# Function to clean the dataset
def clean_marriage_data(df):
    # Step 1: Convert TIME_PERIOD to datetime format
    try:
        df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m', errors='coerce')
    except Exception as e:
        print(f"Error converting TIME_PERIOD to datetime: {e}")
  
    # Step 2: Check for missing values and handle them
    # Display missing value counts
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Drop rows where key columns have missing data
    df = df.dropna(subset=['CIVIC_CENTRE', 'MARRIAGE_LICENSES', 'TIME_PERIOD'])

    # Step 3: Convert MARRIAGE_LICENSES to integer, ensure no negative values
    df['MARRIAGE_LICENSES'] = df['MARRIAGE_LICENSES'].astype(int)
    df = df[df['MARRIAGE_LICENSES'] >= 0]

    # Step 4: Standardize CIVIC_CENTRE names (example: remove whitespace, uppercase)
    df['CIVIC_CENTRE'] = df['CIVIC_CENTRE'].str.upper().str.strip()

    # Step 5: Drop duplicates if any
    df = df.drop_duplicates()

    # Display the cleaned data info
    print("\nCleaned Data Info:")
    print(df.info())

    # Display a preview of the cleaned dataset
    print("\nPreview of Cleaned Data:")
    print(df.head())

    return df

# Main function to load and clean data
def main():
    # Load the data
    # Replace with your actual CSV file path
    file_path = 'data/raw_data/raw_license_data.csv'  
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Clean the data
    cleaned_df = clean_marriage_data(df)

    # Save the cleaned data to a new CSV file
    cleaned_df.to_csv('data/analysis_data/cleaned_marriage_data.csv', index=False)
    print("Cleaned data saved to 'cleaned_marriage_data.csv'.")

# Run the script
if __name__ == "__main__":
    main()
