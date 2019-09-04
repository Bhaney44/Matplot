#Matplot lib from a csv

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#Numpy array
x, y = np.loadtxt('file_name.csv',
                  unpack = True,
                  delimiter = ',')

plt.plot(x,y)

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
