n = int(input())
stack = []
stack_size = 0

def run_cmd_width_stack(cmd, my_stack):
    cmd_type = cmd[0]
    if cmd_type == "push":
        my_stack.push(int(cmd[1]))
    elif cmd_type == "pop":
        my_stack.pop()
    elif cmd_type == "size":
        my_stack.size()
    elif cmd_type == "empty":
        my_stack.empty()
    elif cmd_type == "top":
        my_stack.top()

class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def push(self, x):
        self.stack.append(int(x))
        self.stack_size += 1

    def pop(self):
        if self.stack_size > 0:
            print(stack.pop())
            self.stack_size-=1
        else: print(-1)
    def size(self):
        print(self.stack_size)
    def empty(self):
        if self.stack_size > 0 :
            print(0)
        else:
            print(1)
    def top(self):
        if self.stack_size > 0 :
            print(self.stack[stack_size-1])
        else:
            print(-1)
my_stack = Stack()
for _ in range(n):
    # "push 2".split() => ["push", "2"]
    #   "size".split() => ["size"]
    
    command = input().split()
    stack, stack_size = run_cmd_width_stack(command, my_stack)