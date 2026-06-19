import cv2

image = cv2.imread("logo.jpg")

# Resize
resized = cv2.resize(image, (400, 400))

# Rotate
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotate_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, rotate_matrix, (w, h))

# Crop
crop = image[50:300, 100:400]

# Blur
blur = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original", image)
cv2.imshow("Resized", resized)
cv2.imshow("Rotated", rotated)
cv2.imshow("Cropped", crop)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

