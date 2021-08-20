# 1)

def decimal_conv(i, num_str, b):
    if i == len(num_str):
        return 0

    s_num = len(num_str)-1-i

    if num_str[i].isnumeric():
        num_val = int(num_str[i])
    else:
        num_val = ord(num_str[i]) - ord('A') + 10

    return num_val * (b ** s_num) + decimal_conv(i+1, num_str, b)

num_str, b = input().split()
print(decimal_conv(0, num_str, int(b)))

# 2)

# def decimal_conv_dict(i, num_str, b, char_dict):
#     if i == len(num_str):
#         return 0

#     s_num = len(num_str)-1-i

#     return char_dict[num_str[i]] * (b ** s_num) + decimal_conv_dict(i+1, num_str, b, char_dict)

# char_dict = {}

# for i in range(36):
#     if i < 10:
#         char_dict[str(i)] = i
#     else:
#         char_dict[chr(i-10+ord('A'))] = i

# num_str, b = input().split()
# print(decimal_conv_dict(0, num_str, int(b), char_dict))