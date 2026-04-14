import cv2

img = cv2.imread("b_c.jpg")

# Increase brightness (value can be from 0 to 100)
brightness = 50
bright = cv2.convertScaleAbs(img, beta=brightness)

# Increase contrast (value can be from 1.0 to 3.0)
contrast = 1.5
high_contrast = cv2.convertScaleAbs(img, alpha=contrast)

cv2.imshow("Original", img)
cv2.imshow("Brighter Image", bright)
cv2.imshow("High Contrast Image", high_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()
