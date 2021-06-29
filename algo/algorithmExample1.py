# 숫자 N이 주어졌다.
# N 으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합이 얼마인지 찾는 문제를 풀어보자

#ex) N = 1일 경우 해당하는 자연수는 없기에 0 으로 간주한다.

# N = 2일 경우 3,
# N = 3일 경우 12
# N = 4일 경우 30

def solution(n):
    if n == 1:
        return 0
    elif n > 1:
        # 루프 제한
        limit = n * n
        #조건 부합하는 리스트
        list_data = []
        for i in range(1, limit):
            # 몫
            m = i // n
            # 나머지
            nmg = i % n
            if m == nmg:
                list_data.append(i)
    print(sum(list_data))

def solution2(n):
    sum = 0
    if n == 1:
        return 0
    else:
        for i in range(1,n):
            #sum = i * (n+1)
            sum += n * i + i
    print(sum)

#가우스 합을 이용하여 구하는 공식
def solution3(n):
    #가우스합
    gaus = n * (n+1) / 2
    #배열의 몫 갯수 구하기
    nums = n-1
    print(gaus * nums)
solution(3)
solution2(4)
solution3(5)