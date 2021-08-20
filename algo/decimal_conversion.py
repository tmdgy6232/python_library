# ZZZZZ 36
# 60466175

# 0: 36^4
# 1: 36^3
# 2: 36^2
# 3: 36^1
# 4: 36^0

num_str, b = input().split()

# 1)
# print(int(num_str, int(b)))

# 2)
decimal_result = 0

# 2-2)
# char_dict = {'0': 0, '1': 1, ..., '9': 9, 'A': 10, 'B': 11, ..., 'Z': 35}
char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(num_str)):
    s_num = len(num_str) - 1 - i

    if num_str[i].isnumeric():
        num_val = int(num_str[i])
    else:  # elif ord('A') <= ord(num_str[i]) <= ord('Z'):
        num_val = ord(num_str[i]) - ord('A') + 10

    # 2-2)
    # num_val = char_dict[num_str[i]]
    # num_val = char_map_str.index(num_str[i])

    decimal_result += num_val * (int(b) ** s_num)

print(decimal_result)
