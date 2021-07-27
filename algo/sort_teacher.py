import numpy as np

def insertion_sort(num_list):
    # 각각의 요소를 이미 정렬된 앞 배열부분과 비교하여 삽입한다.
    bef_s_list = num_list.copy()

    # for idx, num in enumerate(bef_s_list):
    for idx in range(len(bef_s_list)):
        now_idx = idx
        # for문 사용
        for now_idx in range(idx, 0 , -1):
            if bef_s_list[now_idx-1] <= bef_s_list[now_idx]:
                break
            bef_s_list[now_idx], bef_s_list[now_idx - 1] = bef_s_list[now_idx - 1], bef_s_list[now_idx]

        # while문 사용
        # while now_idx > 0  and bef_s_list[now_idx-1] > bef_s_list[now_idx]:
        #     bef_s_list[now_idx], bef_s_list[now_idx-1] = bef_s_list[now_idx-1], bef_s_list[now_idx]
        #     print(bef_s_list)
        #     now_idx -= 1

    return bef_s_list

def selection_sort(num_list):

    bef_s_list = num_list.copy()

    for i in range(len(bef_s_list)):
        # min_idx = i
        # for j in range(i, len(bef_s_list)):
        #     if bef_s_list[j] < bef_s_list[min_idx]:
        #         min_idx = j
        min_val = min(bef_s_list[i:])
        min_idx = bef_s_list.index(min_val)

        min_idx = np.argmin(bef_s_list)

    bef_s_list[0], bef_s_list[min_idx] = bef_s_list[min_idx], bef_s_list[0]

    return []

def bubble_sort():
    return []

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort()
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))