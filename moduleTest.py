from myModule.phoneModule import phone as a

print(a.dictData)
s = a.SmartPhone(**a.dictData)
s.turnOn()