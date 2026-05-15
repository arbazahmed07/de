# Q9:
# A) Hive:
# 1. Create database 'shopping'
# 2. Create table 'shopping1'
# 3. Load data from local file (shop.txt)
# 4. Display table data

# ------------------------------------------------------
# Hive Commands

"""
-- Create database
CREATE DATABASE shopping;

-- Use database
USE shopping;

-- Create table
CREATE TABLE shopping1(
    id INT,
    product STRING,
    price INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

-- Load data from local file
LOAD DATA LOCAL INPATH '/path/shop.txt'
INTO TABLE shopping1;

-- Display data
SELECT * FROM shopping1;
"""

# B. Implement LDA (Use packages that are applicable) for the given data and find that best 
# line (linear discriminant) that separates apples and oranges.

# Q9:
# Implement LDA for separating Apples and Oranges

import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# ------------------------------------------------------
# Dataset

data = {
    'Weight': [150, 160, 130, 140],
    'Color_Intensity': [7, 6, 4, 3],
    'Fruit': ['Apple', 'Apple', 'Orange', 'Orange']
}

df = pd.DataFrame(data)

# Features (X)
X = df[['Weight', 'Color_Intensity']]

# Target (y)
y = df['Fruit']

# ------------------------------------------------------
# Apply LDA

lda = LinearDiscriminantAnalysis()

lda.fit(X, y)

# Transform data
X_lda = lda.transform(X)

# ------------------------------------------------------
# Results

print("LDA Transformed Data:")
print(X_lda)

print("\nBest Linear Discriminant Coefficients:")
print(lda.coef_)

print("\nIntercept:")
print(lda.intercept_)