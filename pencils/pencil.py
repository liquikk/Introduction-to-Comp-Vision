import numpy as np
import cv2

min_area = 250000  
max_area = 400000  
num_pencils = 0

for i in range(1,13):
    image = cv2.imread(f'images/{i}.jpg')

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([120, 255, 255])

    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    lower_orange = np.array([0, 100, 100])  
    upper_orange = np.array([20, 255, 255])  

    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_orange = cv2.inRange(hsv_image, lower_orange, upper_orange)

    arr = np.ones((5, 5), np.uint8)
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, arr)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, arr)
    mask_orange = cv2.morphologyEx(mask_orange, cv2.MORPH_CLOSE, arr)

    final_mask = cv2.bitwise_or(mask_blue, cv2.bitwise_or(mask_green, mask_orange))
    contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            num_pencils += 1
    
print("Общее кол-во карандашей:", num_pencils)
# result = cv2.bitwise_and(image, image, mask=final_mask)
# cv2.namedWindow("Result", cv2.WINDOW_GUI_NORMAL)
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(result)
# plt.show()