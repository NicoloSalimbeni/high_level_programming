"""exercise 6 week 4"""
# ead this and plot the data:
# https://www.dropbox.com/s/7u3lm737ogbqsg8/mushrooms_categorized.csv?dl=1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://www.dropbox.com/s/7u3lm737ogbqsg8/mushrooms_categorized.csv?dl=1")
print(df)

classif = df["class"]
classif.hist()
plt.show()
