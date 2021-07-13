class Stack:
    def __init__(self, n):
        self.stack = [None for _ in range(n)]
        self.stack_size = 0


    def push(self, num):
        # self.stack.append(int(num))
        self.stack[self.stack_size] = int(num)
        self.stack_size += 1


    def pop(self):
        if self.size() > 0:
            last_val = self.top()
            self.stack[self.stack_size - 1] = None
            self.stack_size -= 1
            return last_val
        return -1
    # 2)
    # last_val = self.top()
    # if last_val > 0:
    #     self.stack_size -= 1

    # return last_val

    def size(self):
        return self.stack_size


    def empty(self):
        if self.size() > 0:
            return 0

        return 1

    # return int(self.stack_size <= 0)

    def top(self):
        if self.stack_size > 0:
            return self.stack[self.stack_size - 1]

        return -1


def run_cmd_with_stack(my_stack, cmd):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd  # num = cmd[1]
        my_stack.push(num)
    elif cmd_type == "pop":
        print(my_stack.pop())
    elif cmd_type == "size":
        print(my_stack.size())
    elif cmd_type == "empty":
        print(my_stack.empty())
    elif cmd_type == "top":
        print(my_stack.top())
    return my_stack

n = int(input())
my_stack = Stack(n)
for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    my_stack = run_cmd_with_stack(my_stack, command)
print(my_stack.stack)
print(f"stack_size: {my_stack.stack_size}")