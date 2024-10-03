import numpy as np, cv2

image = cv2.imread("mandrillRGB.jpg", cv2.IMREAD_COLOR)

image = cv2.inRange(image, (20, 53, 226), (60, 93, 255))

cv2.imshow("display", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
