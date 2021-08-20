def convert_from_dec(q, b):
    if q == 0:
        return ""

    q, r = divmod(q, b)

    if r < 10:
        target_char = str(r)
    else:
        target_char = chr(r-10+ord('A'))

    return convert_from_dec(q, b) + target_char

n, b = map(int, input().split())

print(convert_from_dec(n, b))