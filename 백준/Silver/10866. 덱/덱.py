import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if 'push_front' in command:
        a, b = command.split()
        q.appendleft(b)

    elif 'push_back' in command:
        a, b = command.split()
        q.append(b)

    elif 'pop_front' in command:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'pop_back' in command:
        if q:
            print(q.pop())
        else:
            print(-1)

    elif 'front' in command:
        if q:
            print(q[0])
        else:
            print(-1)
    elif 'back' in command:
        if q:
            print(q[-1])
        else:
            print(-1)
    elif 'size' in command:
        print(len(q))

    elif 'empty' in command:
        if q:
            print(0)
        else:
            print(1)
