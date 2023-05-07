"""exercise 4 week 7.2"""
# FFT of a simple dataset
# Performe a periodicity analysis on the lynxs-hares population
# I do it only for one of the 2 popoluations, 2 other is the same
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

data = np.loadtxt("./data/populations.txt")
data = data.T

sig_fft = fftpack.fft(data[1])
power = np.abs(sig_fft)

time_step = 1  # 1 year
sample_freq = fftpack.fftfreq(data[1].size, d=time_step)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].plot(data[0], data[1])
ax[0].set_xlabel('year')
ax[0].set_ylabel('hares')

ax[1].plot(sample_freq, power)
ax[1].set_xlabel('Frequency [Hz]')
ax[1].set_ylabel('power')

plt.show()
