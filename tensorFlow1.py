import matplotlib.pyplot as plt  
import numpy as np 

x = [1, 3, 5, 6.5, 7, 12]
y = [1, 4, 6, 8, 9, 14]
plt.plot(x, y, 'ro')
plt.axis([0, 15, 0, 15])
[0, 15, 0, 15]
plt.show()
#predict value
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()