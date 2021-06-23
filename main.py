import random as r

request = input('로또를 얼마 구매하시겠습니까? (숫자만 입력해주세요) ')

number = int(request) / 1000

for a in range(int(number)):
    lottoset = set([])
    while len(lottoset) < 6:
        data = r.randint(1, 45)
        if data not in lottoset:
         lottoset.add(data)
    lottolist = list(lottoset)
    lottolist.sort()
    print(lottolist)
