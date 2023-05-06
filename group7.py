from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

#loading data into ndarray
data =  np.loadtxt("dataset.txt", dtype=float)
print(data)

fig, axs = plt.subplots(1,1, figsize=(10,7), tight_layout = True)

#Add x,y gridlines
axs.grid(  color = 'grey',linestyle = '-.', linewidth = 0.5, alpha = 0.6)
# Plotting the histogram.
plt.hist(data, bins=30, density=True, alpha=0.6, color='green', edgecolor = 'black')

#Calculating mean and standard deviation
mean = stat.mean(data)
std = stat.stdev(data)

#Probability Density Function plot
#xmin, xmax = plt.xlim()
plt.xlim(3,18)
xmin,xmax = 3,18
plt.xticks(range(3,18))
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x,mean, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Group 7 - Normal Distribution"
plt.title(title)
plt.show()
