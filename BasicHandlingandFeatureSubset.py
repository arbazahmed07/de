# Q2:
# A) Implement Basic Data Handling Commands:
# 1. List column names
# 2. Change column names
# 3. Bind rows
# 4. Bind columns
# 5. Find missing values

import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# 1. List column names
print(df.columns)

# 2. Change column names
df.rename(columns={"old_name": "new_name"}, inplace=True)

# 3. Bind rows
df1 = df
df2 = df
df_rows = pd.concat([df1, df2], axis=0)

# 4. Bind columns
df_cols = pd.concat([df1, df2], axis=1)

# 5. Find missing values
print(df.isnull())
print(df.isnull().sum())


# Implement Feature Extraction (Use packages that are applicable) using Feature Subset 
# Selection (Visualize Correlation using Heatmap) 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()

# Create dataframe
df = pd.DataFrame(data.data, columns=data.feature_names)

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()

# Feature subset selection
selected = df[['petal length (cm)', 'petal width (cm)']]

print(selected.head())