#### Preamble ####
# Purpose: Simulates... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 11 February 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####

# [...UPDATE THIS...]

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(423)

# Simulate the data
n_rows = 100  # Number of rows you want to simulate

# Generate an ID column starting from a random large number to mimic the structure
id = np.arange(15381, 15381 + n_rows)

# Generate Civic Centres randomly
civic_centres = np.random.choice(['ET', 'NY', 'SC', 'TO', 'YK'], size=n_rows)

# Generate number of marriage licenses using a Poisson distribution
# Lambda is set to 100 as an average number of licenses; adjust as necessary
marriage_licenses = np.random.poisson(lam=100, size=n_rows)

# Generate random time periods (monthly data for several years)
time_periods = pd.date_range(start='2011-01-01', periods=n_rows, freq='M').strftime('%Y-%m')

# Create the DataFrame
df = pd.DataFrame({
    '_id': id,
    'CIVIC_CENTRE': civic_centres,
    'MARRIAGE_LICENSES': marriage_licenses,
    'TIME_PERIOD': time_periods
})

# Display the first few rows of the DataFrame
print(df.head())

# Optionally save the DataFrame to a CSV file
df.to_csv('data/simulated_marriage_data.csv', index=False)
print("Simulated data saved to 'simulated_marriage_data.csv'")
