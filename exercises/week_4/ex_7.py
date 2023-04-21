"""exercisie 7 week 4"""
# Load the remote file:
# https://www.dropbox.com/s/vkl89yce7xjdq4n/regression_generated.csv?dl=1
# with Pandas and plot a scatter plot all possible combination of the
# following fields:

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/vkl89yce7xjdq4n/regression_generated.csv?dl=1")

features_1 = df["features_1"]
features_2 = df["features_2"]
features_3 = df["features_3"]

# multiplot
fig, axes = plt.subplots(1, 3)

axes[0].scatter(features_1, features_2)
axes[0].title.set_text("1,2")
axes[1].scatter(features_1, features_3)
axes[1].title.set_text("1,3")
axes[2].scatter(features_2, features_3)
axes[2].title.set_text("2,3")
plt.show()
