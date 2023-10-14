import numpy as np

img1 = "txts/img1.txt"
img2 = "txts/img2.txt"

img1_data = np.loadtxt(img1, skiprows=1)
img2_data = np.loadtxt(img2, skiprows=1)

img1_firstPoint = np.argwhere(img1_data == 1)
img2_firstPoint = np.argwhere(img2_data == 1)

y = abs(img2_firstPoint[0][0] - img1_firstPoint[0][0])
x = abs(img2_firstPoint[0][1] - img1_firstPoint[0][1])
print("Смещение по y = ",y,", cмещение по x = ",x)