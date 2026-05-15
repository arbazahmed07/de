# Q7:
# HDFS Operations:
# 1. Create a file in local environment
> hdfs dfs -mkdir /hadooplab 
> gedit fu.txt 

# 2. Display content of file
>cat fu.txt

# 3. Move (upload) file to Hadoop (HDFS)
> hdfs dfs -put fu.txt /hadooplab

# 4. Verify file in HDFS
>  hdfs dfs -ls /hadooplab

# 5. Display file content from HDFS
> hdfs dfs -cat /hadooplab/fu.txt

''' 
b) # Q:
# Implement Basic Statistical Functions for Data Exploration
# 1. Measures of Central Tendency: Mean, Median, Mode
# 2. Dispersion: Variance, Standard Deviation
# 3. Position: Quartiles and Inter-Quartile Range (IQR)

import pandas as pd
import numpy as np

# Load dataset (own choice)
df = pd.read_csv("data.csv")

# ------------------------------------------------------
# 1. Measures of Central Tendency

# Mean
mean_val = df['column_name'].mean()

# Median
median_val = df['column_name'].median()

# Mode
mode_val = df['column_name'].mode()

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)


# ------------------------------------------------------
# 2. Dispersion of Data

# Variance
variance_val = df['column_name'].var()

# Standard Deviation
std_val = df['column_name'].std()

print("Variance:", variance_val)
print("Standard Deviation:", std_val)


# ------------------------------------------------------
# 3. Quartiles and IQR

# Quartiles
Q1 = df['column_name'].quantile(0.25)
Q2 = df['column_name'].quantile(0.50)   # Median
Q3 = df['column_name'].quantile(0.75)

# Interquartile Range
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("IQR:", IQR)



'''