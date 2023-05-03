"""exercise 11 week 7"""
# PCA on 3D dataset
#
#     Generate a dataset with 3 features each with N entries (N being ).
#     With the normali distribution with mean and standard deviation,
#     generate the 3 variables such that:
#
#        𝑥1 is distributed as 𝑁(0,1)
#        𝑥2 is distributed as 𝑥1+𝑁(0,3)
#        𝑥3 is given by 2𝑥1+𝑥2
#
#  -Find the eigenvectors and eigenvalues of the covariance matrix of the
#       dataset
#  -Find the eigenvectors and eigenvalues using SVD. Check that they are two
#       procedure yields to same result
#  -What percent of the total variability is explained by the principal
#       components?
#  -Given how the dataset was constructed, do these make sense? Reduce the
#       dimensionality of the system so that at least 99% of the total
#       variability is retained.
#  -Redefine the data in the basis yielded by the PCA procedure
#  -Plot the data points in the original and the new coordiantes as a set
#   of scatter plots. Your final figure should have 2 rows of 3 plots each,
#   where the columns show the (0,1), (0,2) and (1,2) proejctions.

import numpy as np
import matplotlib.pyplot as plt

N = 3000

x1 = np.random.normal(size=N)
x2 = np.random.normal(loc=0, scale=3, size=N)
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
