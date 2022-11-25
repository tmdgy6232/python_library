# 5
# 4 1 5 2 3
# 5
# 1 3 5 7 9

def find_by_b_search(find_num, nums):
    # 3 (0 1 2) => 1
    # 8 (0 1 2 3 4 5 6 7) => 4
    start_idx = 0
    end_idx = len(nums) - 1
    mid_idx = (start_idx + end_idx) // 2

    while start_idx <= end_idx:
        if nums[mid_idx] > find_num:
            end_idx = mid_idx-1
        elif  nums[mid_idx] < find_num:
            start_idx = mid_idx+1
        else :
            return mid_idx

def find_by_b_search_recursion(find_num, nums, start_idx, end_idx):

    if start_idx > end_idx:
        return -1

    mid_idx = (start_idx + end_idx) // 2
    if nums[mid_idx] > find_num:
        return find_by_b_search_recursion(find_num, nums, start_idx, mid_idx-1)
    elif nums[mid_idx] < find_num:
        return find_by_b_search_recursion(find_num, nums, mid_idx+1, end_idx)
    return mid_idx

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

m = int(input())

for target_num in map(int, input().split()):
    if find_by_b_search_recursion(target_num,num_list, 0, n-1) >= 0:
        print('1')
    else:
        print('0')
