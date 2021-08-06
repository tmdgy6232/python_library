from collections import deque

n = int(input())
d_list = deque([i for i in range(1, n+1)])

rotate_flag = False
print('init : ', d_list)
while len(d_list) > 1:
    d_list.popleft()
    print(d_list)
    d_list.append(d_list.popleft())
    print(d_list)
    #d_list.rotate(-1) # 이동시키기

    # if not rotate_flag:
    #     d_list.popleft()
    # else:
    #     d_list.append(d_list.popleft())
    # rotate_flag = not rotate_flag

