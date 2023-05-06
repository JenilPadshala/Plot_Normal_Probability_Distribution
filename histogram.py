import numpy as np
import matplotlib.pyplot as plt
#loading data into ndarray
data =  np.loadtxt("dataset.txt", dtype=float)
fig, axs = plt.subplots(1,1, figsize=(10,7), tight_layout = True)
#Add x,y gridlines
axs.grid(  color = 'grey',linestyle = '-.', linewidth = 0.5, alpha = 0.6)
# Plotting the histogram.
plt.hist(data, bins=30, density=True, alpha=0.6, color='green', edgecolor = 'black')
plt.xticks(range(3,18))
title = "Group 7 - Normal Distribution"

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title(title)
plt.show()
