import cv2

image = cv2.imread("b_c.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Thresholding (Binary)
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Color Mask (detect red color)
lower_red = (0, 100, 100)
upper_red = (10, 255, 255)
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("Binary Threshold", thresh)
cv2.imshow("Red Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
