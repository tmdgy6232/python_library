from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())

min_move_cnt = 0
num_list = deque([i for i in range(1, n+1)])


for find_num in target_list:
    find_idx = num_list.index(find_num)
    move_cnt = find_idx # 왼쪽으로 옮기는 횟수

    if find_idx > len(num_list) - find_idx:
        move_cnt -= len(num_list)

    min_move_cnt += abs(move_cnt)
    num_list.rotate(-move_cnt)
    num_list.popleft()
    print(num_list)
    print(move_cnt)
    # num_list.append(num_list.popleft()) # num_list.rotate(-)
    # num_list.appendleft(num_list.pop()) # num_list.rotate(+)

print(min_move_cnt)