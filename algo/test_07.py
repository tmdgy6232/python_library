import numpy as np
import pandas as pd
#weight = AB
#y = OPS
#y_hat = Pred

batterA = ['A', 200, 0.9, 0.95]
batterB = ['B', 50, 0.4, 0.35]
batterC = ['C', 0, 0.0, 0.5]
batterD = ['D', 0, 0.0, 0.3]

total_list = np.asarray([batterA, batterB, batterC, batterD])

class WRMSE:
    def __init__(self, data):
        self.data = data
    def print_result(self):
        wrmse_row = []
        self.sumWeight()
        for i in range(len(self.data)):
            wrmse = self.calculate(self.data[i])
            wrmse_row.append(wrmse)
        result = sum(wrmse_row)
        #str_round_result = str(result)[:8]
        print(round(result, 6))
        print(np.round(result, 6))
        np.round(result, 6)# 4자리까지밖에 안나옴
        return result#float((str_round_result))

    def sumWeight(self): # 가중치 합 구하기
        weightList = self.data[:,1]
        weightList_int = np.array(weightList, np.int32)
        self.sumWeight_val = weightList_int.sum()

    def calculate(self, listData): #시그마 안의 식 구하기
        y = float(listData[2])
        y_hat = float(listData[3])
        weight = int(listData[1])
        return np.sqrt(((y - y_hat)**2) * weight / self.sumWeight_val)


wirmse = WRMSE(total_list)
print(wirmse.print_result())

a = [1,2,3,4]
help(a)