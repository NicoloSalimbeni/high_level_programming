"""exercisi 3 week 7"""
# Looking at an oscillating spring (optional)
#
# Imagine you have cameras looking at a spring oscillating along the axis.
# Each camera record the motion of the spring looking at it along a
# given direction defined by the pair, the angles in spherical
# coordinates.
# Start from the simulation of the records (say) of the spring's motion
# along the x axis, assuming a little random noise affects the
# measurements along the. Rotate such dataset to emulate the records
# of each camera.
# Perform a Principal Component Analysis on the thus obtained dataset, aiming
# at finding the only one coordinate that really matters.

import numpy as np
import matplotlib.pyplot as plt

omega = 1
A = 1
N = 1000
t = np.arange(0, 20, 20 / N)

x = A * np.sin(omega * t)

y = np.random.normal(scale=1 / 10, size=N)

position_xy = np.array([x, y]).T

ncam = 10
cam_sphdir = [[np.random.rand() * 2 * np.pi,
               np.random.rand() * np.pi] for i in range(ncam)]

cam_cartdir_xy = np.array(
    [[np.sin(sph[0]) * np.cos(sph[1]),
      np.sin(sph[0]) * np.sin(sph[1])] for sph in cam_sphdir])

cam_records = np.array([[np.dot(camdir, pos) for pos in position_xy]
                        for camdir in cam_cartdir_xy])
plt.figure()
for record in cam_records:
    plt.plot(t, record)
plt.title('Camera records')
plt.show()

U, spectrum, Vt = np.linalg.svd(cam_records)

eigval = spectrum
explained_var = eigval / np.sum(eigval)

print('fraction of variability explained per principal component:',
      explained_var)

records_pc = np.dot(U.T, cam_records)

plt.figure()
plt.title('principal components of camera records dataset')
plt.plot(t, records_pc[0], label='firs p.c.')
plt.plot(t, records_pc[1], color='r', label='second p.c.')
plt.xlabel('time')
plt.ylabel('principal components')
plt.legend()
plt.show()
