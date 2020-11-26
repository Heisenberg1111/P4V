#!/usr/bin/python3


# graph using matplotlib pyplot function

# November 26 2020


import matplotlib.pyplot as plt

x = [ i for i in range(10)]
print(x)
y=[2*i for i in range(10)]
print(y)

plt.xlabel('x-axis') # label for the x-axis of the graph
plt.ylabel('y-axis') # label for the y-axis of the graph
plt.scatter(x,y) # plot the data
plt.show() # show the graph in a UI. If not called, the graph will not be shown
