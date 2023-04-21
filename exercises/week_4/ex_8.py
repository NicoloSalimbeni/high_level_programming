"""exercise 8 week 4"""
# Load the same file of point 6, and convert the file to json with Pandas:
# https://www.dropbox.com/s/7u3lm737ogbqsg8/mushrooms_categorized.csv?dl=1

import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/7u3lm737ogbqsg8/mushrooms_categorized.csv?dl=1")
df = df.to_json("mushrooms.json")
