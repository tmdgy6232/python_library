import math
def example1(n): # 약수구하기
    div_num_list = []
    for i in range(1, n+1):
        if n % i == 0:
            div_num_list.append(i)
    print(div_num_list)

def example2(nums): # 최댓값 최소값 구하기

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print(f'최댓값 : {nums[0]} 최솟값 : {nums[-1]}')

def example2_2(nums):
    max_value = 0
    min_value = 9
    for i in nums:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    print(f'최댓값 : {max_value} 최솟값 : {min_value}')

def example1_teacher(num):

    #sqrt_num = int(math.sqrt(num))
    sqrt_num = int(num ** (1/2))

    front_divisor_list = []
    rear_divisor_list = []

    for i in range(1, sqrt_num+1):
        if num % i == 0:
            front_divisor_list.append(i)
            if i != int(num/i):
                rear_divisor_list.append(int(num/i))
    print(front_divisor_list + rear_divisor_list[::-1])

example1(100)
example1_teacher(100)
example2([5,10,15,3, 40, 1, 70])
example2_2([5,10,15,3, 40, 1, 70])
