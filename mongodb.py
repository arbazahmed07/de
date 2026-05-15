// Q10: Create a database and work with MongoDB Query Language (Book Database)

// a) Creating a Database and Collection
use bookdb
db.createCollection("books")

// b) Insert Documents

// Insert a single document
db.books.insertOne({
  title: "DSA",
  author: "Pavan",
  price: 500
})

// Insert multiple documents
db.books.insertMany([
  {title: "DBMS", author: "John", price: 400},
  {title: "OS", author: "Smith", price: 300}
])

// c) Find All Books & Find with Condition

// Find all books
db.books.find()

// Find books with condition (price > 350)
db.books.find({price: {$gt: 350}})

// d) Update One Book & Multiple Books

// Update one book
db.books.updateOne(
  {title: "DSA"},
  {$set: {price: 600}}
)

// Update multiple books
db.books.updateMany(
  {},
  {$set: {publisher: "ABC"}}
)

// e) Delete Documents (One & Multiple Books)

// Delete one book
db.books.deleteOne({title: "OS"})

// Delete multiple books
db.books.deleteMany({price: {$lt: 400}})



# SVD

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

df = pd.DataFrame(X)

U, S, Vt = np.linalg.svd(df, full_matrices=False)

# Plot first two components
plt.scatter(U[:,0], U[:,1], c=y)
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.title("SVD")
plt.show()