import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion


trajectories = []

for i in range(100):
    h_area = np.load(f"out/h_{i}.npy")

    labeled = label(binary_erosion(h_area))

    props = regionprops(labeled)

    frame_trajectory = []
    for prop in props:
        centroid = prop.centroid
        frame_trajectory.append(centroid)
    trajectories.append(frame_trajectory)

trajectories = np.array(trajectories)

plt.figure(figsize=(8, 8))

for i in range(trajectories.shape[1]):
    plt.plot(trajectories[:, i, 1], trajectories[:, i, 0], label=f"Object {i + 1}")

plt.title("Траектории движения объектов")
plt.legend()
plt.show()