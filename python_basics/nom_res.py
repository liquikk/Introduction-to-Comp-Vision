import numpy as np


def calculate_resolution(img):
    image = np.loadtxt(img, dtype=int, skiprows=1)
    max_size = np.loadtxt(img, dtype=int, max_rows=1)
    resolution = max_size / image.shape[1]
    return resolution

image_files = ["txts/figure1.txt", "txts/figure2.txt", "txts/figure4.txt", "txts/figure5.txt", "txts/figure6.txt"]

for image_file in image_files:
    resolution = calculate_resolution(image_file)
    print(f"Номинальное разрешение для {image_file} = {resolution} мм/пиксель")