from collections import deque

deque_obj = deque()
print(type(deque_obj))
print(deque_obj)

deque_obj.append(10)
deque_obj.append(20)
deque_obj.appendleft(100)
deque_obj.appendleft(200)
print(deque_obj)