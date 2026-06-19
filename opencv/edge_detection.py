import cv2

image = cv2.imread("logo.jpg", 0)  # read in grayscale

# Canny Edge Detection
edges = cv2.Canny(image, 100, 200)

# Sobel Filter
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

# Laplacian Filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow("Original", image)
cv2.imshow("Canny", edges)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
