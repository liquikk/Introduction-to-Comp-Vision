import cv2
import numpy as np

def count_frames_with_image(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_orange = np.array([0, 50, 50])
        upper_orange = np.array([20, 255, 255])

        lower_red = np.array([165, 50, 50])
        upper_red = np.array([180, 255, 255])

        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        lower_light_brown = np.array([10, 50, 50])
        upper_light_brown = np.array([30, 255, 255])

        mask_orange = cv2.inRange(hsv_frame, lower_orange, upper_orange)
        mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
        mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        mask_light_brown = cv2.inRange(hsv_frame, lower_light_brown, upper_light_brown)

        combined_mask = cv2.bitwise_or(cv2.bitwise_or(cv2.bitwise_or(mask_blue, mask_orange), mask_red), mask_light_brown)
        selected_frames = cv2.bitwise_and(frame, frame, mask=combined_mask)

        if cv2.countNonZero(mask_blue) > 0 and cv2.countNonZero(mask_orange) > 0 and cv2.countNonZero(mask_red) > 0 and cv2.countNonZero(mask_light_brown) > 500:
            # cv2.imshow("asd", selected_frames)
            # cv2.waitKey()
            frame_count += 1

    cap.release()
    # cv2.destroyAllWindows()
    return frame_count

video_path = 'vid/output.avi'
frame_count_with_image = count_frames_with_image(video_path)

print("Количество кадров с моим изображением:", frame_count_with_image)
