#Generate Visualization

import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

##plot takes an arbitrary number of arguments.


#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.show()

##Formatting the style of your plot
    ##For every x, y pair - there is a string for color
    ##The axis() command takes a list of
        ## [xmin, xmax, ymin, ymax] and specifies the viewport

#plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()

##numpy

#import numpy as np

#t = np.arange(0., 5., 0.2)

#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()


##Plotting with categorical variables

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

         
