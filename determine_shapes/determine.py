import cv2
import numpy as np
from skimage.measure import label

def count_shapes_by_colors(image_path):
    image = cv2.imread(image_path)

    gr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    labeled = label(gr)
    totall = np.max(labeled)
    print("Всего объектов на изображении:", totall)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([40, 60, 50])
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    lower_yellow = np.array([20, 50, 50])
    upper_yellow = np.array([40, 255, 255])

    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])
    
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    pink_mask = cv2.inRange(hsv_image, lower_pink, upper_pink)

    masks=[blue_mask, green_mask, red_mask, yellow_mask, pink_mask]
    colors=["синие","зелёные","красные","жёлтые","розовые"]
    i = 0
    for mask in masks:

        result = cv2.bitwise_and(image, image, mask=mask)

        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rect = 0
        circle = 0
        total_color = 0
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
            if len(approx) == 4:
                rect += 1
            else:
                circle += 1
            total_color += 1
    
        print(f'{colors[i]} :')
        print(f'всего объектов: {total_color}')
        print(f'прямоугольников: {rect}')
        print(f'кругов: {circle}')
        i += 1
    
count_shapes_by_colors("image/balls_and_rects.png")