"""exercise 9 week 3"""
# Analyze a data file
#     -Download the population of hares, lynxes and carrots at the beginning of
#     the last century.
#         wget https://www.dropbox.com/s/3vigxoqayo389uc/populations.txt
#     -Check the content by looking within the file
#     -Load the data (use an appropriate numpy method) into a 2D array
#     -Create arrays out of the columns, the arrays being (in order): year,
#     hares, lynxes, carrots
#     -Plot the 3 populations over the years
#     -Compute the main statistical properties of the dataset (mean, std,
#     correlations, etc.)
#     -Which species has the highest population each year?
#
# Do you feel there is some evident correlation here? Studies tend to believe so.

import numpy as np
import matplotlib.pyplot as plt

raw_data = np.loadtxt('populations.txt')

dataset = raw_data.transpose()

# plot the 3 populations all together
figure, axis = plt.subplots(1, 3)

# plot hares
axis[0].plot(dataset[0], dataset[1])
axis[0].set_title("(year,hares)")
axis[0].set_xlabel("year")
axis[0].set_ylabel("hares")

# plot hares
axis[1].plot(dataset[0], dataset[2])
axis[1].set_title("(year,lynxes)")
axis[1].set_xlabel("year")
axis[1].set_ylabel("lynxes")

# plot hares
axis[2].plot(dataset[0], dataset[3])
axis[2].set_title("(year,carrots)")
axis[2].set_xlabel("year")
axis[2].set_ylabel("carrots")

plt.show()

# highest population each year
for i in range(0, len(dataset[0])):
    if dataset[1, i] > dataset[2, i]:
        print("most numerous species in ", int(dataset[0, i]), ": hares")
    else:
        print("most numerous species in ", int(dataset[0, i]), ": lynxes")

# easy statistics
print("\nmean value of hares: ", np.mean(dataset[1]))
print("standard deviations value of hares: ", np.std(dataset[1]))
print("\nmean value of lynxes: ", np.mean(dataset[2]))
print("standard deviations value of lynxes: ", np.std(dataset[2]))
print("\nmean value of carrots: ", np.mean(dataset[3]))
print("standard deviations value of carrots: ", np.std(dataset[3]))
