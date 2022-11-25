# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

n = int(input())
meet_time = []
for _ in range(n):
    start_time, end_time = map(int, input().split())
    meet_time.append([end_time, start_time])

meet_time.sort()
print(meet_time)

result_meet_cnt = 1
last_meet_end_time = meet_time[0][0]

for meet in meet_time[1:]:
    start_time, end_time = meet
    if last_meet_end_time <= start_time:
        last_meet_end_time = end_time
        result_meet_cnt += 1

print(result_meet_cnt)