# Q1: 
# A) Implement Basic Data Handling Commands:
# 1. Read data from CSV file
# 2. Find dimension of data
# 3. Display top 5 rows and full data

import pandas as pd

# Read data from CSV file
df = pd.read_csv("data.csv")

# Find dimension of data
print(df.shape)

# Display top 5 rows
print(df.head())

# Display full data
print(df)


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

