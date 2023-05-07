"""exercise 5 week 7.2"""

# -Examine the provided image moonlanding.png, which is
# heavily contaminated with periodic noise. In this exercise,
# we aim to clean up the noise using the Fast Fourier Transform.
# -Load the image using pylab.imread().
# -Find and use the 2-D FFT function in scipy.fftpack, and plot the
# spectrum (Fourier transform of) the image. Do you have any trouble
# visualising the spectrum? If so, why?
# -The spectrum consists of high and low frequency components. The
# noise is contained in the high-frequency part of the spectrum,
# so set some of those components to zero (use array slicing).
# -Apply the inverse Fourier transform to see the resulting image.

import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

# plot the image
im = plt.imread('./data/moonlanding.png')
fig, ax = plt.subplots(2, 2, figsize=(13, 10))
ax[0, 0].imshow(im, cmap="Greys_r")
ax[0, 0].set_title("Original image")

# compute fft
im_fft = fftpack.fft2(im)

# plot fft
all_freq = ax[0, 1].imshow(np.abs(im_fft), norm='log', vmin=5)
plt.colorbar(all_freq, ax=ax[0, 1])
ax[0, 1].set_title("Fourier transform")

# since high frequencies are in the middle of the furier trasform image
# we keep only the corners of the plot.

keep_fraction = 0.1
im_fft2 = im_fft.copy()
rows, columns = im_fft2.shape  # row = pixel y, columns = pixel x
im_fft2[int(rows * keep_fraction):int(rows * (1 - keep_fraction))] = 0
im_fft2[:, int(columns * keep_fraction):int(columns * (1 - keep_fraction))] = 0

low_freq = ax[1, 1].imshow(np.abs(im_fft2), norm='log', vmin=5)
plt.colorbar(low_freq, ax=ax[1, 1])
ax[1, 1].set_title("Low frequencies")

# reconstruct the image with only low frequencies
im_new = fftpack.ifft2(im_fft2).real
ax[1, 0].imshow(im_new, cmap="Greys_r")
ax[1, 0].set_title("Fixed image")

plt.show()
