number_list1 = [1, 2, 4]
number_list2 = [1, 2, 7, 6, 4]

def solution(nums):
    answer = []
    for i in range(len(nums)):
        firstNum = nums[i]
        copy_nums = nums.copy()
        copy_nums.pop(i)
        for j in range(len(copy_nums)):
            secondNum = copy_nums[j]
            last_nums = copy_nums.copy()
            last_nums.pop(j)
            for k in range(len(last_nums)):
                thirdNum = last_nums[k]
                numberList = [firstNum, secondNum, thirdNum]
                answer.append(numberList)
    temp = "".join(answer)
    print(temp)


    return answer

solution(number_list1)
solution(number_list2)

