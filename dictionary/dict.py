import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

def has_vline_1(arr):
    return 1.0 in arr.mean(0)

def has_vline_B(prop):
    img = prop.image
    mean = img.mean(0)
    if np.any(mean[:1] == 1):
        return 1
    
def mean_vert(prop):
    image = prop.image
    mean = image.mean(1)
    if np.any(mean == 1):
        return 1
    
def mean_hor(prop):
    image = prop.image
    mean = image.mean(0)
    if np.any(mean == 1):
        return 1

def crop_euler(prop, crop_size):
    half_height = int(prop.image.shape[0] / crop_size)
    cropped_image = prop.image[:half_height, :]
    cropped_props = regionprops(label(cropped_image))
    cropped_euler_number = cropped_props[0].euler_number
    return cropped_euler_number

def recognize(prop):
    euler_number = prop.euler_number
    if euler_number == -1:
        if has_vline_B(prop):
            return "B"
        else:
            return "8"
    elif euler_number == 0:
        y,x = prop.centroid_local
        y /= prop.image.shape[0]
        x /= prop.image.shape[1]
        cropped_euler_number = crop_euler(prop, 1.55)
        if mean_vert(prop):
            return '*'
        if cropped_euler_number == 0:
            return "P"
        elif np.isclose(x,y,0.06):
            return "0"
        else:
            cropped_euler_number = crop_euler(prop, 1.4)
            if cropped_euler_number == 0:
                return "A"
            else:
                return "D"
    else:
        if prop.image.mean() == 1.0:
            # print("-")
            return "-"
        else:
            if mean_hor(prop) and prop.eccentricity > 0.5:
                return "1"
            else:
                tmp = prop.image.copy()
                tmp[[0, -1], :] = 1
                tmp[:, [0,-1]] = 1
                tmp_labeled = label(tmp)
                tmp_props = regionprops(tmp_labeled)
                tmp_euler = tmp_props[0].euler_number
                if tmp_euler == -3:
                    return "X"
                
                elif tmp_euler == -1:
                    return "/"
                else:
                    if prop.eccentricity > 0.5:
                        return "W"
                    else:
                        return "*"
    return "_"
    
image = plt.imread("images/symbols.png")
image = image.mean(2)
image = image > 0
labeled = label(image)
print("Всего символов:",np.max(labeled))
 
props = regionprops(labeled)
result = {}
for prop in props:
    symbol = recognize(prop)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
print(result)
print("Распознано",(1 - result.get("_",0) / np.max(labeled)) * 100, "% символов")