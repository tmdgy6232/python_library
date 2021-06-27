def comb(population,num):
    ans = []
    #정의된 값인지 확인한다.
    if num > len(population): return ans

    #base case
    if num == 1:
        for i in population:
            ans.append(i)
    #General Case:
    elif num > 1:
        for i in range(len(population)-num+1): #i 가 시작하는값 - len(population) - (n-1)
            for temp in comb(population[i+1:], num-1):
                print(temp)
    return ans

#print(comb([1,2,3,4,5], 3))

data = [i for i in range(5)]
print(data)
