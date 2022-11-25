# 그리디 알고리즘 (욕심쟁이, 탐욕알고리즘)
# 매 순간 최적으로 판단되는 선택을 이어나가 최종 해답에 도달함
# 즉 일반적으로 Locally Optimized한 선택을 이어나가지만 최종 해답이 Optimized하다고 확실할 순 없다.

kind_num, total = map(int,input().split())

coin_kind_price = [1, 5, 10, 50, 100, 500, 1000, 5000]
coin_kind_price.reverse()
# 1) 반복문 사용

# for i in range(kind_num):
#     coin_price = int(input())
#     coin_kind_price.append(coin_price)
#
# result_coin_num = 0
#
# coin_kind_price.reverse()
#
# for coin in coin_kind_price:
#     # 값이 다 채워지면 반복문 나가기
#     if total == 0:
#         break
#     # 몫이 1보다 클 경우에만 계산하여 result_coin_num을 추가해준다.
#     if total / coin >= 1:
#         result_coin_num += total // coin
#         total -= total // coin * coin
#print(result_coin_num)

# 2) 재귀사용

def cal_coin(i, coin_kind_price, total):
    if i == len(coin_kind_price):
        return 0

    return total // coin_kind_price[i] + cal_coin(i+1, coin_kind_price, total - coin_kind_price[i] * (total // coin_kind_price[i]))

print(cal_coin(0, coin_kind_price, total))