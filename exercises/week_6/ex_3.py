"""exercise 3 week 6"""

# Produce a profile plot from a scatter plot.
#
#     -Download the following dataset and load it as a pandas dataframe:
# wget https://www.dropbox.com/s/hgnvyj9abatk8g6/residuals_261.npy
#
# Note that you should you the np.load() function to load the file as a numpy
# array and then pass it to the pd.DataFrame() constructor.
#
#     -Inspect the dataset, you'll find two variables (features)
#     -Clean the sample by selecting the entries (rows) with the variable
#     "residual" in absolute value smaller than 2
#     -perform a linear regression of "residuals" versus "distances"
#     using scipy.stats.linregress()
#     -plot a seaborn jointplot of "residuals" versus "distances", having
#     seaborn performing a linear regression. The result of the regression
#     should be displayed on the plot
#     -Fill 3 numpy arrays
#         -x, serving as an array of bin centers for the "distance" variable.
#         It should range from 0 to 20 with reasonable number of steps (bins)
#         -y, the mean values of the "residuals", estimated in slices (bins)
#         of "distance"
#         -erry, the standard deviation of the of the "residuals", estimated
#         in slices (bins) of "distance"
#     Plot the profile plot on top of the scatter plot

import pandas as pd
import seaborn as sns
import numpy as np
import scipy
import matplotlib.pyplot as plt

data = np.load("./data/residuals_261.npy", allow_pickle=True)
df = pd.DataFrame(data.item())
df = df[abs(df["residuals"]) < 2]
result = scipy.stats.linregress(df["distances"], df["residuals"])

# fill x array
x = np.linspace(0, 19, 19) + 0.5
bin_width = x[1] - x[0]
y = [0] * len(x)
yerr = [0] * len(x)

for i in range(0, len(x)):
    tmp_df = df[abs(df["distances"] - x[i]) < bin_width / 2]
    y[i] = tmp_df["residuals"].mean()
for i in range(0, len(x)):
    tmp_df = df[abs(df["distances"] - x[i]) < bin_width / 2]
    yerr[i] = tmp_df["residuals"].std()

sns.jointplot(x="distances",
              y="residuals",
              data=df,
              kind="reg",
              line_kws={
                  'color': 'orange',
                  "lw": 3
              })
plt.errorbar(x, y, yerr=yerr, color='orange')

plt.show()
