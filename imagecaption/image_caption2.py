import cv2
from image_caption3 import make_image
# Read input image
img = cv2.imread('testimg.png', cv2.IMREAD_COLOR)
# img = cv2.imread('output2.png', cv2.IMREAD_COLOR)

# Convert to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Simple threshold
_, thr = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Morphological closing to improve mask
close = cv2.morphologyEx(255 - thr, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))

# Find only outer contours
contours, _ = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Save images for large enough contours
areaThr = 3000
i = 0
middle_img = None

for cnt in contours:
    area = cv2.contourArea(cnt)
    if (area > areaThr):
        i = i + 1
        x, y, width, height = cv2.boundingRect(cnt)
        if i > 1:
            middle_img = img[y:y+height-1, x:x+width-1]

make_image(middle_img)