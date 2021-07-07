stack = []
stack_size = 0
# len, index-1을 쓰지말고 구현

def solution(command, stack, stack_size):
    if 'push' in command:
        x = int(command.split()[1])
        stack_size += 1
        _stack = [0 for i in range(stack_size+1)]
        _stack = stack + [x]
        stack = _stack
    elif 'pop' == command:
        if stack:
            print(stack[stack_size-1])
            _stack = [0 for i in range(stack_size - 1)]
            _stack = stack[:stack_size-1]
            stack = _stack
            stack_size -= 1
        else:
            print(-1)
    elif 'size' == command:
        if stack:
            print(stack_size)
        else: print(0)
    elif 'empty' == command:
        if stack: print(0)
        else: print(1)
    elif 'top' == command:
        if stack: print(stack[stack_size -1])
        else: print(-1)
    return stack, stack_size
n = int(input())

for i in range(n):
    command = input()
    stack, stack_size = solution(command, stack, stack_size)
