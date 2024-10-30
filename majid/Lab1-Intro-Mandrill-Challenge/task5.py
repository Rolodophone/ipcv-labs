import numpy as np, cv2

original = cv2.imread("mandrillRGB.jpg", cv2.IMREAD_UNCHANGED)

mandrill0 = cv2.imread("mandrill0.jpg", cv2.IMREAD_UNCHANGED)

for y in range(mandrill0.shape[0]):
    for x in range(mandrill0.shape[1]):
        before = np.copy(mandrill0[y, x])
        mandrill0[y, x, 2] = before[1]
        mandrill0[y, x, 0] = before[2]
        mandrill0[y, x, 1] = before[0]


mandrill1 = cv2.imread("mandrill1.jpg", cv2.IMREAD_UNCHANGED)

mandrill1[:, :, 2] = np.roll(mandrill1[:, :, 2], (30))
mandrill1[31:, :, 2] = mandrill1[:481, :, 2]


cv2.imshow("display", mandrill1)
cv2.waitKey(0)
cv2.destroyAllWindows()
