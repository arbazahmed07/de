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


# PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target


# ------------------------------------------------------
# 1. PCA (Principal Component Analysis)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA")
plt.show()

