import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation,
                                binary_opening, binary_closing)
from skimage.measure import label

stars = np.load("stars.npy")

mask_cross =  np.array([[1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0],
                        [1, 0, 0, 0, 1]])

mask_plus =   np.array([[0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [1, 1, 1, 1, 1],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0]])


labeled = label(stars)
cross = label(binary_erosion(labeled, mask_cross))
n_cross = len(np.unique(cross)) - 1
print("звёзд в виде X:",n_cross)
plus = label(binary_erosion(labeled, mask_plus))
n_plus = len(np.unique(plus)) - 1
print("звёзд в виде +:",n_plus)
print("всего звёзд:", n_plus+n_cross)
# plt.imshow(stars)
# plt.show()