n, b = map(int, input().split())
result_list = []
q = n

char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while q > 0:
    q, r = divmod(q, b)
    # 1)
    if r < 10:
        result_list.append(str(r))
    else:
        # r => 10 ~ 35
        # r-10 => 0 ~ 25
        # r-10+ord('A') => ord('A') ~ ord('Z')
        # chr(r-10+ord('A')) => 'A' ~ 'Z'

        result_list.append(chr(r - 10 + ord('A')))

    # 2)
    # result_list.append(char_map_str[r])

print("".join(result_list[::-1]))