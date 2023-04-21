"""exercise 1 week 5"""
# Create a Pandas DataFrame by read N raws of the 'data_000637.txt' dataset.
# Choose N to be smaller than or equal to the maximum number of raws and
# larger that 10k.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) import the data inside a data frame
df = pd.read_csv("./data/data_000637.csv")

# 2)Find out the value of 'x'
x = df.describe()['BX_COUNTER']['max']
print(x)

# 3) Find out how much the data taking lasted. You can either make an estimate
# on the baseis of the fraction of the measurements (raws) you read, or perform
# this check precisely by reading out the whole dataset
tot_time = (int(df.max()["ORBIT_CNT"]) - 3869200167) * x * 25
print("Total time (ns):", tot_time)
print("Total time (sec):", (tot_time / 10**9))

# 4) Create a new column with the actual time in ns (as a combination of the
# other three columns with timing information)
df['time_ns'] = df['TDC_MEAS'] * 25 / 30 + df['BX_COUNTER'] * 25 + x * df[
    "ORBIT_CNT"] * 25

# 5) Replace the values (all 1) of the HEAD column randomly with 0 or 1.
length = len(df)
randomHead = np.random.randint(2, size=length)
df["HEAD"] = randomHead

# 6) Create a new DataFrame that contains only the rows with HEAD=1.
df_head1 = df[df["HEAD"] == 1]
print(df_head1)

# 7) Make two occupancy plots (one per FPGA), i.e. plot the number of
# counts per TDC channel

fpga_0_counts = df[df["FPGA"] == 0]["TDC_CHANNEL"]
fpga_1_counts = df[df["FPGA"] == 1]["TDC_CHANNEL"]
n_ch = int(df.describe()['TDC_CHANNEL']['max'])

fig, axes = plt.subplots(1, 2)
fpga_0_counts.plot.hist(bins=n_ch, ax=axes[0])
axes[0].title.set_text("FPGA 0")
fpga_1_counts.plot.hist(bins=n_ch, ax=axes[1])
axes[1].title.set_text("FPGA 1")
plt.show()

# 8) Use the groupby method to find out the noisy channels, i.e. the
# TDC channels with most counts (say the top 3)
print(
    "FPGA 0",
    df[df['FPGA'] == 0][['TDC_CHANNEL',
                         'time_ns']].groupby('TDC_CHANNEL').count().nlargest(
                             3, 'time_ns'))
print(
    "FPGA 1",
    df[df['FPGA'] == 1][['TDC_CHANNEL',
                         'time_ns']].groupby('TDC_CHANNEL').count().nlargest(
                             3, 'time_ns'))

# 9)Count the number of unique orbits. Count the number of unique orbits with
# at least one measurement from TDC_CHANNEL=139
print("Numbers of unique orbits:", len(df.groupby('ORBIT_CNT')))
print("Numbers of unique orbits for TDC=139:",
      len(df[df['TDC_CHANNEL'] == 139].groupby('ORBIT_CNT')))
