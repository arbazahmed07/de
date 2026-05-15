# Q13:
# Implement Basic Data Handling Commands

import pandas as pd

# ------------------------------------------------------
# 1. Read data from CSV file

df = pd.read_csv("students.csv")

# ------------------------------------------------------
# 2. Dimension of the data

print("Dimensions of Dataset:")
print(df.shape)

# ------------------------------------------------------
# 3. Display top 5 rows

print("\nTop 5 Rows:")
print(df.head())

# ------------------------------------------------------
# Display complete dataset

print("\nComplete Dataset:")
print(df)


# LDA
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
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit(X, y).transform(X)

plt.scatter(X_lda[:,0], X_lda[:,1], c=y)
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.title("LDA")
plt.show()
