import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# Paint image certain color
# blank[200:300, 300:400] = 0, 255, 0
# cv.rectangle(
#     blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), -1)
# cv.imshow("Rect", blank)

# # Draw Circle
# cv.circle(blank, (250, 250), 40, (0, 0, 255), -1)
# cv.imshow("Circle", blank)

# # Draw Line
# cv.line(blank, (100, 250), (300,
#         400), (255, 255, 255), 3)
# cv.imshow("Line", blank)

# Write Text
cv.putText(blank, "Hello", (0, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)
cv.imshow("Text", blank)
cv.waitKey(0)
