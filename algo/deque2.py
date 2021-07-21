from collections import deque

class StackAndQueue:
    def __init__(self, data_type = "stack"):
        self.array = deque()
        self.data_type = data_type

    def push(self, num):
        self.array.append(num)

    def pop(self, num):
        if self.is_empty():
            return -1

        if self.is_stack():
            return self.array.pop()
        return self.array.popleft()

    def size(self):
        return len(self.array)

    def empty(self):
        return int(self.is_empty())

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if not self.is_stack() or self.is_empty():
            return -1
        return self.array[-1]

    def front(self):
        if self.is_empty() or self.is_stack():
            return -1
        return self.array[0]


    def back(self):
        if self.is_empty() or self.is_stack():
            return -1
        return self.array[-1]

    def is_stack(self):
        return self.data_type == "stack"


def run_command(deque_obj, command):
    commandType = command[0]
    if commandType == "push":
        deque_obj.push(int(command[1]))
    elif commandType == 'pop':
        print(deque_obj.pop())
    elif commandType == 'size':
        print(deque_obj.size())
    elif commandType == 'empty':
        print(deque_obj.empty())
    elif commandType == 'top':
        print(deque_obj.top())
    elif commandType == 'front':
        print(deque_obj.front())
    elif commandType == 'back':
        print(deque_obj.back())
    return None

data_type = input()
n = int(input())
data_obj = StackAndQueue(data_type= data_type)

for _ in range(n):

    command = input().split()

    data_obj = run_command(data_obj, command)