import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('qm_3.csv', delimiter=',', unpack=True)
plt.scatter(x,y, label='Patents')

plt.xlabel('Claims')
plt.ylabel('Cited Proior Art')
plt.title('Patents')
plt.legend()
plt.show()
