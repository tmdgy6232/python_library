import queue

queue = queue.Queue()

class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.frontPoint=0
        self.backPoint=0

    def push(self, num):
        self.queue[self.backPoint] = num
        self.backPoint += 1

    def back(self):
        if  self.size() > 0:
            print(self.queue[self.backPoint-1])
        else: print(-1)

    def front(self):
        if self.size() > 0 :
            print(self.queue[self.frontPoint])
        else:
            print(-1)

    def pop(self):
        if self.size() > 0:
            print(self.queue[self.frontPoint])
            self.frontPoint += 1
        else:
            print(-1)

    def empty(self):
        if self.size() > 0:
            print(0)
        else:
            print(1)

    def size(self):
        return self.backPoint - self.frontPoint


def run_cmd_with_queue(queue, command):
    commandType = command[0]
    if commandType == "push":
        queue.push(int(command[1]))
    elif commandType == "front":
        queue.front()
    elif commandType == "back":
        queue.back()
    elif commandType == "pop":
        queue.pop()
    elif commandType == "empty":
        queue.empty()
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