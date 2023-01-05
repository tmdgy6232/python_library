import cv2

def make_image(img_name):
    # Read input image
    # img = cv2.imread('template2.png', cv2.IMREAD_COLOR)
    img = img_name

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
    resultX = 0
    resultY = 0
    resultW = 0
    resultH = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > areaThr):
            i = i + 1
            x, y, width, height = cv2.boundingRect(cnt)
            if resultY > y or resultY == 0:
                resultY = y
            resultH += height
            resultX = x
            resultW = width

    cv2.imwrite('out.jpg', img[resultY:resultY+resultH+7, resultX:resultX+resultW-1])
