import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_opening

objs = np.load("ps.npy.txt")


obj1 = np.array([[1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1]])

obj2 = np.array([[1,1,1,1,],
                 [1,1,1,1,],
                 [1,1,0,0,],
                 [1,1,0,0,],
                 [1,1,1,1,],
                 [1,1,1,1,]])

obj3 = np.array([[1,1,1,1],
                 [1,1,1,1],
                 [0,0,1,1],
                 [0,0,1,1],
                 [1,1,1,1],
                 [1,1,1,1]])

obj4 = np.array([[1,1,0,0,1,1],
                 [1,1,0,0,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1]])


obj5 = np.array([[1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,0,0,1,1],
                 [1,1,0,0,1,1]])

labeled = label(objs)
n = np.max(labeled)
print("всего объектов: ", n)
n_obj1 = label(binary_opening(objs, obj1)).max()
n_obj2 = label(binary_opening(objs, obj2)).max()
n_obj3 = label(binary_opening(objs, obj3)).max()
n_obj4 = label(binary_opening(objs, obj4)).max() - label(binary_opening(objs, obj1)).max() #горизонтальные объекты с дыркой также захватывают гор. объекты без дырки
n_obj5 = label(binary_opening(objs, obj5)).max() - label(binary_opening(objs, obj1)).max() #горизонтальные объекты с дыркой также захватывают гор. объекты без дырки

print("кол-во объектов 1 вида: ",n_obj1)
print("кол-во объектов 2 вида: ",n_obj2)
print("кол-во объектов 3 вида: ",n_obj3)
print("кол-во объектов 4 вида: ",n_obj4)
print("кол-во объектов 5 вида: ",n_obj5)