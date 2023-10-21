import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation,
                                binary_opening, binary_closing)
from skimage.measure import label

wires = np.load("wires6.npy")
struct = np.ones((3,1))

labeled = label(wires)
new_image = np.zeros_like(wires)
new_image[labeled==3] = 1

for lb in range(1, np.max(labeled)+1):
    new_image = np.zeros_like(wires)
    new_image[labeled==lb] = 1
    print("провод №",lb)
    a = binary_erosion(new_image,struct)
    n = 1
    for i in a:
        for j in i:
            if i[0] == True:
                if j == False:
                    n += 1
            else:
                n = 0
    if n == 1:
        print("целый")
    elif n == 0:
        print("провод умер")
    else:
        print("порван на",n,"частей")


plt.subplot(121)
plt.imshow(label(wires))
plt.subplot(122)
plt.imshow(binary_erosion(wires,struct))
plt.show()