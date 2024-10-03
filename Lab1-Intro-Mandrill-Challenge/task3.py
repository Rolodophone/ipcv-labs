import numpy, cv2

image = cv2.imread("mandrill.jpg", cv2.IMREAD_GRAYSCALE)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if 85 < image[y, x] < 115:
            image[y, x] = 255
        else:
            image[y, x] = 0

cv2.imshow("Display", image)
cv2.waitKey(0)
cv2.destroyAllWindows()