class Queue:
    def __init__(self):
        self.queue = []
    def push(self, num):
        self.queue.insert(0 , num)
    def front(self):
        if len(self.queue) > 0:
            print(self.queue[-1])
        else: print(-1)
    def back(self):
        if len(self.queue) > 0:
            print(self.queue[0])
        else:
            print(-1)
    def pop(self):
        if len(self.queue) > 0:
            print(self.queue[-1])
            del self.queue[-1]
        else:
            print(-1)
    def empty(self):
        if len(self.queue) > 0:
            print(0)
        else:
            print(-1)
    def size(self):
        print(len(self.queue))


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
my_queue = Queue()
for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    my_queue = run_cmd_with_queue(my_queue, command)