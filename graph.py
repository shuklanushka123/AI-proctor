import matplotlib.pyplot as plt
import time
import random
 
x_data_arr = []
y_data_arr = []
 
plt.show()
 
axes = plt.gca()
axes.set_xlim(0, 100)
axes.set_ylim(0,1)
line, = axes.plot(x_data_arr, y_data_arr, color='bo')
 
for i in range(100):
    x_data_arr.append(i)
    y_data_arr.append(i/2)
    line.set_xdata(x_data_arr)
    line.set_ydata(y_data_arr)
    plt.draw()
    plt.pause(1e-17)
 
# add this if you don't want the window to disappear at the end
plt.show()