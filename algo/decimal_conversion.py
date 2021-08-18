
num_str, b = input().split()
b = int(b)


#1)
#print(int(num_str, int(b)))

#2)
decimal_result = 0
for i in range(0, len(num_str)):
    s_num = len(num_str)-1-i

    if num_str[i].isnumeric():
        num_val = int(num_str[i])
    else: #elif ord('A') <= ord(num_str[i])
        num_val = ord(num_str[i]) - ord('A') + 10
    decimal_result += num_val * b ** s_num
print(decimal_result)


