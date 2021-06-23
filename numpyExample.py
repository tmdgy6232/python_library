import numpy as np
from PIL import Image
from myModule.phoneModule import phone

temp = np.zeros((3,2,1))

temp[2][0][0] = 1

temp = np.zeros((2, 5, 3))

temp[0][3][1] = 1

temp = np.zeros((7,2))
temp[1][0] = 1

#배열만들기
np_array = np.array([1,2,3.0])

np_array = np.array([ (1,2,3), (4,5,6) ])

np_array = np.full_like((2,5,5), 11)

np_array = np.arange(1, 10, 0.1)

np_array = np.linspace(10, -5, num=14)

arr = np.array([[1,2,3], [7,8,9]])
arr1 = np.array([[4,5,6],[10, 11, 12]])

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6]])

sum = np.concatenate((arr1, arr2.T), axis=1)

arr1 = np.zeros((3,5,4))
arr2 = np.ones((3,5,1))

img = np.asarray(Image.open('lena.png'))
img = img.copy()
img2 = img.copy()

img = np.concatenate((img, img2), 1)
img = np.concatenate((img, img), 0)
img = Image.fromarray(img,'RGB')
#print(type(img))
#img.show()

arr = np.array([[[1, 4, 20, 23, 28], [13, 8, 24, 21, 5]], [[19,15,11, 22,0], [6, 16, 7, 17, 12]],[[25,29,26,18,2], [14,27,9,10,3]]])
arr = np.delete(arr, (0,1),2)


img = np.asarray(Image.open('lena.png'))

img = img.copy()
img2 = img.copy()

img = np.delete(img, np.s_[100:300], 0)
img = Image.fromarray(img,'RGB')
#img.show()

arr_example = np.array([[[1, 4, 20, 23, 28], [13, 8, 24, 21, 5]], [[19,15,11, 22,0], [6, 16, 7, 17, 12]],[[25,29,26,18,2], [14,27,9,10,3]]])

img = np.asarray(Image.open('lena.png'))
img = img.copy()
img = img.reshape(256, 1024, 3)
img = Image.fromarray(img,'RGB')

arr = np.arange(50).reshape(2,5,5)


img = np.asarray(Image.open('lena.png'))
img = img.copy()
img = img[300:100:-1, 500:250:-1, :]
img = Image.fromarray(img,'RGB')

arr[arr < 10] = 100

img = np.asarray(Image.open('lena.png'))
img = img.copy()
img[img >= 100] = 255
img = Image.fromarray(img,'RGB')

arr = np.array(range(6))

arr2 = arr[np.newaxis, :]
arr3 = arr[:,np.newaxis]

arr = np.array(range(20)).reshape(4,5)
arr2 = arr[:,:,np.newaxis]

arr = np.array(range(20))
arr2 = np.expand_dims(arr, axis=0)

arr = np.array(range(3))

arr = arr[:, np.newaxis] + arr

arr1 = np.array([[1,1], [2,2]])
arr2 = np.array([[3,3], [4,4]])

arr_vstack = np.vstack((arr1, arr2))

arr_hstack = np.hstack((arr1, arr2))

arr = np.arange(1, 25).reshape(2, 12)

arr1, arr2, arr3 = np.hsplit(arr,(3,4))

arr1 = np.array(range(20)).reshape(4,5)

arr2 = arr1.view()
arr2[0] = 999

arr1 = np.array([1,2])
arr2 = np.ones(2, dtype=int)

arr = np.arange(1, 25).reshape(6, 4)
arr1 = np.arange(1,17).reshape(4,4)

arr1 = np.array([[1,0], [0,1]])
arr2 = np.array([[4,1], [2,2]])

#행렬곱 이해해라
arr = np.array([1, 2])

arr = np.array([[0],[10],[20],[30]])
arr1 = np.array([[0,1,2]])

arr = np.arange(9)
np.random.shuffle(arr)

arr = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20])
unique_val, countdata = np.unique(arr, return_index=True)

arr_2d = np.array([[1,2,3,3], [5,6,3,3],[7,8,3,3],[1,2,3,3]])
unique_row = np.unique(arr_2d, axis=0)
unique_cols = np.unique(arr_2d, axis=1)

arr = np.arange(4).reshape(2,2)


arr = np.array(range(8)).reshape(2,4)

reversed_arr = np.flip(arr, axis=1)

arr = np.array([[1,2], [3,4],[5,6]])

arr = np.array([1,2,3,4,5,6])
np.save('npArrayTest', arr)

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3,4,5,6])
np.savez('npArrayTest1', arr1, arr2)

np.savetxt('new_npFile.csv', arr)

arr_npy = np.load('./npArrayTest.npy')

arr_txt = np.loadtxt('new_npFile.csv')

arr_test = np.load('./npArrayTest1.npz')['arr_0']

arr = np.array((range(12))).reshape(2,2,3)
arr = np.transpose(arr, (2,1,0))
print(arr)
print(arr.shape)
