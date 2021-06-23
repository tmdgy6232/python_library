import numpy as np

npArray = np.array([1,2,3])

arr2 = np.array([(1, 2, 3), (1.5, 2.5, 3.5)])

arr3 = np.array([1.5, 3, 5], dtype=np.int64)
#기본적으로 생성된 배열(array)의 dtype 은 float64 이 기본값입니다.

arr_zeros = np.zeros(3)
#2차원 이상 배열을 만들때는 매개변수를 튜플로 넣어야한다.
arr_zeros = np.zeros((3, 4))

#사용법은 zeros와 같다
arr_ones = np.ones(3, dtype=np.int64)

#Python에서는 빈 리스트를 만들 수 있지만 Numpy의 array는 그렇지 않습니다. 빈 배열을 만들어
#주고 싶을 때는 np.empty() 를 이용하여 크기를 지정해 주어야 합니다. np.empty()로 생성한 배
#열은 메모리 상태에 따라 무작위의 값이 들어있습니다. 나중에 용도에 따라 원소를 채워주면 됩니다
arr_empty = np.empty(3)

#np.arange() 는 주어진 범위에서 균일한 간격의 값을 갖는 배열(array)을 생성합니다.
arr = np.arange(4)
arr = np.arange(2, 9, 2)
arr = np.arange(1, 100, 10)

#np.linspace() 는 지정된 범위에서 균등한 간격의 숫자를 반환합니다.
arr = np.linspace(0, 10, num =19)

'''
배열의 원소를 정렬할 때는 np.sort()를 사용하여 정렬할 수 있습니다. np.sort()는 정렬된 배열의 
복사본을 반환하게 됩니다. 함수를 호출할 때 축, 종류, 순서를 지정할 수 있습니다. 아무것도 지정하
지 않으면 기본으로 오름차순 정렬이 이루어집니다
 argsort : 하나 이상의 키를 기준으로 데이터 정렬
• lexsort : 여러 키를 기준으로 데이터 정렬(나중에 넘겨준 배열이 기준이 되어 데이터 정렬)
• searchsorted : 정렬된 배열에서 요소를 찾습니다.
• partition : 부분 정렬
'''

'''arr1 이라는 배열이 있고, arr2 라는 배열이 있을 때 np.concatenate() 를 사용하여 두 배열을 이
어붙여서 하나의 배열을 만들 수 있습니다.'''

arr1 = np.array([[1, 2], [3,4]])
arr2 = np.array([[5, 6]])

arr_concat = np.concatenate((arr1, arr2), axis=0)
arr1 = np.array(list(range(0,6)))
arr2 = np.reshape(arr1, (1,6))
'''
다차원 인덱싱, 슬라이싱
'''

arr = np.arange(10).reshape(2, 5)


arr = np.arange(20).reshape(5,4)
print(arr)
print(arr[:3,1:3])