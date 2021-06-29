
def solution():
    a, b, r = input('공사현장의 좌표, 소음거리를 적어주세요 ex) 20 10 10').split(' ')
    a, b, r = int(a), int(b), int(r)
    n = input('그늘의 수를 적어주세요 : ')
    n_list = []

    for i in range(int(n)):
        x_i, y_i = input('그늘의 x, y 좌표를 적어주세요 : ex) 10 10').split(' ')
        n_list.append([int(x_i),int(y_i)])

    for i in n_list:
        x_i, y_i = i

        cal = ((x_i-a)**2) + ((y_i - b) **2)
        if cal >= (r**2):
            print('silent')
        else:
            print('noisy')

def solution_teacher():
    a, b, r = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        if (x-a)**2 + (y-b)**2 >= r**2:
            print('silent')
        else:
            print('noisy')
solution()