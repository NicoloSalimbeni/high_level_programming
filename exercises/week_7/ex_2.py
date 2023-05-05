"""exercise 2 week 7"""
# Start from the dataset you have genereted in the previous exercise and add
# uncorrelated random noise. Such noise should be represented by other 10
# uncorrelated variables normal distributed, with standar deviation much
# smaller (say, a factor 50) than those used to generate the 𝑥1 and 𝑥2.
# Repeat the PCA procedure and compare the results with what you obtained before

import numpy as np
import matplotlib.pyplot as plt

N = 3000

x1 = np.random.normal(size=N)
x2 = np.random.normal(loc=0, scale=3, size=N)
x3 = 2 * x1 + x2
noise_vec = [np.random.normal(loc=0, scale=1 / 50, size=N) for x in range(10)]

for noise in noise_vec:
    x1 = x1 + noise
    x2 = x2 + noise
    x3 = 2 * x1 + x2

data = np.array([x1, x2, x3])

cov = np.cov(data)

print("covariant matrix:")
print(cov)

U, spectrum, Vt = np.linalg.svd(cov)
eigv, eigvec = np.linalg.eig(cov)
eigv_svd = spectrum
print("\n")
print("eigenvalues:")
print(eigv)
print("eigenvalues SVD:")
print(spectrum)
print("eigenvectors:")
print(eigvec)
print("eigenvectors SVD:")
print(U)

explined_var = eigv_svd / sum(eigv_svd)

print("\n")
print("fraction of variability explained per principal component: ",
      explined_var)
print(
    "so we need the first 2 components to mantain 99% of the total variability"
)

data_pca = np.dot(U.T, data)

fig, ((plt01, plt02, plt12), (plt01pca, plt02pca,
                              plt12pca)) = plt.subplots(nrows=2,
                                                        ncols=3,
                                                        figsize=(16, 8))
plt01.scatter(x=data[0], y=data[1], marker='o', c='r', edgecolor='black')
plt01.set_xlabel('x1')
plt01.set_ylabel('x2')

plt12.scatter(x=data[1], y=data[2], marker='o', c='g', edgecolor='black')
plt12.set_xlabel('x2')
plt12.set_ylabel('x3')

plt02.scatter(x=data[0], y=data[2], marker='o', c='b', edgecolor='black')
plt02.set_xlabel('x1')
plt02.set_ylabel('x3')

plt01pca.scatter(x=data_pca[0],
                 y=data_pca[1],
                 marker='o',
                 c='r',
                 edgecolor='black')
plt01pca.set_xlabel('first p.c.')
plt01pca.set_ylabel('second p.c.')
plt01pca.set_ylim([-7, 7])

plt12pca.scatter(x=data_pca[1],
                 y=data_pca[2],
                 marker='o',
                 c='g',
                 edgecolor='black')
plt12pca.set_xlabel('second p.c.')
plt12pca.set_ylabel('third p.c.')
plt12pca.set_ylim([-7, 7])

plt02pca.scatter(x=data_pca[0],
                 y=data_pca[2],
                 marker='o',
                 c='b',
                 edgecolor='black')
plt02pca.set_xlabel('first p.c.')
plt02pca.set_ylabel('third p.c.')
plt02pca.set_ylim([-7, 7])

plt.show()
