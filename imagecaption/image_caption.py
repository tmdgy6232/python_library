import cv2
import os

def make_image(img, file_first_name):
    # Read input image
    # img = cv2.imread('template2.png', cv2.IMREAD_COLOR)
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

    cv2.imwrite('result_image/'+file_first_name+'_cut.jpg', img[resultY-2:resultY-2+resultH+5, resultX-2:resultX-2+resultW+3])

def make_middle_image(file_name):
    # Read input image
    img = cv2.imread(file_name, cv2.IMREAD_COLOR)
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
    return middle_img

file_list = os.listdir('original_image')

for file_name in file_list:
    original_file_name = 'original_image/'+file_name
    if file_name.count(".") == 1:
        name = file_name.split('.')[0]
        file_first_name = name
    else:
        for k in range(len(file_name) - 1, 0, -1):
            if file_name[k] == '.':
                file_first_name = file_name[:k]
                break
    middle_img = make_middle_image(original_file_name)
    make_image(middle_img, file_first_name)