from itertools import permutations, combinations
number_list1 = [1,2,4]
number_list2 = [1,2,7,6,4]
def solution(nums):
    answer = []
    ss_list = []
    for i in list(combinations(nums,3)):
        isBool = False
        for j in range(2,sum(i)):
            if sum(i) % j == 0:
                isBool = True
        if not isBool:
            ss_list.append(i)
    print(ss_list)
    return answer

solution(number_list1)
solution(number_list2)