n = 1000 - int(input())
coin_list = [500,100,50,10,5,1]

# 1) iteration
# result_cnt = 0

# for coin in coin_list:
#     result_cnt += n // coin
#     n %= coin

# print(result_cnt)

# 2) recursion

def calc_coin(i, coin_list, remain):
    if i == len(coin_list):
        return 0

    return remain // coin_list[i] + calc_coin(i+1, coin_list, remain % coin_list[i])

print(calc_coin(0, coin_list, n))