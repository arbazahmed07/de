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




# Create a partition (shopping3) for table shopping1 and also create 3 buckets inside each 
# partition, check your partition 

-- Step 1: Create shopping1 table
CREATE TABLE shopping1 (
    id INT,
    product STRING,
    price DOUBLE,
    category STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


-- Step 2: Create shopping3 table
CREATE TABLE shopping3 (
    id INT,
    product STRING,
    price DOUBLE
)
PARTITIONED BY (category STRING)
CLUSTERED BY (id) INTO 3 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


ALTER TABLE shopping3 ADD PARTITION (category='electronics');
ALTER TABLE shopping3 ADD PARTITION (category='clothes');
ALTER TABLE shopping3 ADD PARTITION (category='grocery');

SHOW PARTITIONS shopping3;
DESCRIBE FORMATTED shopping3;

