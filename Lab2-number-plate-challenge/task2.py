import numpy as np
import cv2
from task1 import convolution_colour

input_image = cv2.imread("car1.png", cv2.IMREAD_COLOR)
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
blurred = convolution_colour(input_image, kernel)
diff = input_image - blurred
sharpened = input_image + 0.5 * diff

cv2.imshow("sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()