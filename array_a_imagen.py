import numpy as np
import matplotlib.pyplot as plt

X=np.random.randint(256, size=(10, 10))
print(X)
fig = plt.figure(figsize=(8,6))
plt.imshow(X)
plt.title("Plot 2D array")
plt.colorbar()
plt.savefig("1.png")
'''
https://www.delftstack.com/es/howto/matplotlib/colorplot-of-2d-array-matplotlib/
'''
