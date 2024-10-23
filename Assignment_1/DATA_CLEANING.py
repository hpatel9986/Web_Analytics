import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path = 'D:/WEB ANALYTICS/AssignmenT/'
data = pd.read_csv(path+'Assignment1Data_Sample.csv')

# Step: 1
# Required fields
required_fields = [
    'Object ID', 'Department', 'Object Name', 
    'Title', 'Culture', 'Artist Nationality', 
    'Object Begin Date', 'Object End Date', 
    'Medium', 'Credit Line', 'Country'
]

data = data[required_fields]

# Step: 2
# Trim whitespace from string fields
string_columns = ['Department', 'Object Name', 'Title', 'Culture', 'Artist Nationality', 'Medium', 'Credit Line', 'Country']
data[string_columns] = data[string_columns].apply(lambda x: x.str.strip())

# Step: 3
# change data type for object begin date and object end date 
# Convert date columns to datetime
data['Object Begin Date'] = pd.to_datetime(data['Object Begin Date'], errors='coerce')
data['Object End Date'] = pd.to_datetime(data['Object End Date'], errors='coerce')

# Step: 4
# Check for missing values
missing_values = data.isnull().sum()

# Drop rows with missing values in required fields
data = data.dropna(subset=required_fields)

# Step: 5
# Remove records where Object Begin Date is later than Object End Date
data = data[data['Object Begin Date'] <= data['Object End Date']]

#Step: 6
# create flag for important condition 
data['Country'] = data['Country'].replace({
    'USA': 'United States',
    'U.S.A.': 'United States',
    'UK': 'United Kingdom',
})

# looking at head (5 observations) 
# Final check of the cleaned dataset
print(data.info())
print(data.head())

data.to_csv(path + 'Assignment_1_Data_Clean.csv', index=False)

