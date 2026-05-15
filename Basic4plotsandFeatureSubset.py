# Q3:
# A) Implement Basic Plots for Data Exploration (Iris Dataset):
# 1. Generate box plot for all predictors
# 2. Generate box plot for a specific feature
# 3. Generate histogram for a specific feature
# 4. Generate scatter plot (petal length vs sepal length)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# 1. Box plot for all predictors
sns.boxplot(data=df[['sepal length','sepal width','petal length','petal width']])
plt.show()

# 2. Box plot for specific feature
sns.boxplot(x='class', y='sepal length', data=df)
plt.show()

# 3. Histogram for specific feature
sns.histplot(x='sepal length', data=df)
plt.show()

# 4. Scatter plot
sns.scatterplot(x='petal length', y='sepal length', data=df)
plt.show()





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