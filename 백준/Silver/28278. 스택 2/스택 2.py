import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
stack = deque()

for i in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        stack.append(int(command[1]))

    elif command[0] == 2:
        if not stack:
            print(-1)
        else :
            print(stack.pop())

    elif command[0] == 3:
        print(len(stack))

    elif command[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)

    elif command[0] == 5:
        if not stack:
            print(-1)
        else:
            print(stack[-1])