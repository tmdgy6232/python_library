import queue

queue = queue.Queue()

class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.frontPoint = 0
        self.backPoint = 0

    def push(self, num):
        self.queue[self.backPoint] = num
        self.backPoint += 1

    def back(self):
        if  self.size() > 0:
            return self.queue[self.backPoint-1]
        else: return -1

    def front(self):
        if self.size() > 0 :
            return self.queue[self.frontPoint]
        else:
            return -1

    def pop(self):
        if self.size() > 0:
            # last_val = self.queue[self.frontPoint]
            # self.frontPoint += 1
            # return last_val
            self.frontPoint += 1
            return self.queue[self.frontPoint-1]
        else:
            return -1

    def empty(self):
        if self.size() > 0:
            return 0
        else:
            return 1

    def size(self):
        return self.backPoint - self.frontPoint


def run_cmd_with_queue(queue, command):
    commandType = command[0]
    if commandType == "push":
        queue.push(int(command[1]))
    elif commandType == "front":
        print(queue.front())
    elif commandType == "back":
        print(queue.back())
    elif commandType == "pop":
        print(queue.pop())
    elif commandType == "empty":
        print(queue.empty())
    elif commandType == "size":
        print(queue.size())
    else:
        print('input Error')
        return
    return queue

n = int(input())
my_queue = Queue(n)
for _ in range(n):
    command = input().split()
    my_queue = run_cmd_with_queue(my_queue, command)