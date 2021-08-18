import os
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

## 경로가 중복되어 읽어오지 못한다.
## img = Image.open('AI_STUDY/dataset/flowers/rose/12243068283_ee4c2683e2_n.jpg')
# print(os.getcwd())
img = Image.open('../../dataset/flowers/rose/12243068283_ee4c2683e2_n.jpg')

# print("img : ", img)

img_array = np.array(img)
# print("img_array.shape : \n", img_array.shape)

# resized = img.resize([100,100]) # 이미지 사이즈 조정
# plt.imshow(resized)
# plt.show()

path = '../../dataset/flowers/'  # 패스 설정해서


# print('filenames : ', filenames)


def list_dir(path):  # 파일 리스트 반환 함수
    filenames = os.listdir(path)  # 패스에 있는 폴더 리스트 가져오기
    filenames.sort()
    return filenames

def load_image_pixels(imagepath, resolution):
     img = Image.open(imagepath)
     img.resize(resolution)
     return np.array(img)

# resolution = [100, 100]
# pixels = load_image_pixels(testimage, resolution)
# print(testimage)
# print(pixels.shape)

def flowers_init(resolution):
    path = '../../dataset/flowers/'
    target_names = list_dir(path)

    images, idxs = [], []

    for dx, dname in enumerate(target_names):
        print("dname : ", dname)

        subpath = path + dname
        print("subpath : ", subpath)

        filenames = list_dir(subpath)
        print("filenames : \n", filenames[:3])

        for fname in filenames:
            if fname[-4:] != '.jpg':
                continue

            imagepath = os.path.join(subpath, fname)

            pixels = load_image_pixels(imagepath, resolution)

            images.append(pixels)
            idxs.append(dx)

    xs = np.asarray(images, dtype=np.float32)

    return xs, idxs


xs, idx = flowers_init(resolution=[100,100])
