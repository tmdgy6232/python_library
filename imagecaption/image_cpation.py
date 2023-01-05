
import numpy as np
import cv2
# Read the image
img = cv2.imread('testimg.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 0, 0)

# Create a binary mask
mask = np.zeros_like(edges)
mask[edges != 0] = 1

# Apply the mask to the original image
outlined_image = cv2.bitwise_and(img, img, mask=mask)

# Save the outlined image
cv2.imwrite('outlined_image.jpg', outlined_image)