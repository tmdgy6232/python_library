class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.queuesize = 0
    def push(self, num):
        self.queue.insert(0 , num)
        self.queuesize += 1
    def front(self):
        if self.queuesize > 0:
            print(self.queue[self.queuesize-1])
        else: print(-1)
    def back(self):
        if self.queuesize > 0 :
            print(self.queue[0])
        else:
            print(-1)
    def pop(self):
        if self.queuesize > 0:
            print(self.queue[self.queuesize-1])
            self.queue[self.queuesize-1] = None
            self.queuesize -= 1
        else:
            print(-1)
    def empty(self):
        if self.queuesize > 0:
            print(0)
        else:
            print(1)
    def size(self):
        print(self.queuesize)


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
        queue.size()
    else:
        print('input Error')
        return
    return queue

n = int(input())
my_queue = Queue(n)
for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    my_queue = run_cmd_with_queue(my_queue, command)