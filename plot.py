import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 30, 100)
y = x**3
plt.plot(x, y, label="x**3", color="blue") 
plt.show()
