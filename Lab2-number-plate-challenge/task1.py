import numpy as np
import cv2

def convolution(input_image, kernel):
    output_image = np.zeros(input_image.shape, dtype=np.uint8)
    kernel_radius = round((kernel.shape[0] - 1) / 2)  # note: this assumes kernel is square
    input_padded = np.pad(input_image, kernel_radius, mode='edge')
    kernel = np.flip(kernel)  # flip the kernel in both axes for convolution

    for y in range(input_image.shape[0]):
        for x in range(input_image.shape[1]):
            patch = input_padded[y:y + kernel.shape[0], x:x + kernel.shape[1]]
            output_image[y, x] = (np.multiply(patch, kernel)).sum()

    return output_image


input_image = cv2.imread("mandrill.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3)) / 9

cv2.imshow("Result", convolution(input_image, kernel))
cv2.waitKey(0)
cv2.destroyAllWindows()