"""exercise 1 week 5"""
# Create a Pandas DataFrame by read N raws of the 'data_000637.txt' dataset.
# Choose N to be smaller than or equal to the maximum number of raws and
# larger that 10k.

import pandas as pd

# import the data inside a data frame
df = pd.read_csv("./data/data_000637.csv", nrows=10000)
print(df)
