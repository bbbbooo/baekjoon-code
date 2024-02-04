import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque()
for i in range(n):
    l = sys.stdin.readline().rstrip()

    if 'push' in l:
        a, b = l.split()
        q.append(b)

    elif 'front' in l:
        if q:
            print(q[0])
        else :
            print(-1)
    elif 'back' in l:
        if q:
            print(q[-1])
        else :
            print(-1)
    elif 'empty' in l:
        if q:
            print(0)
        else:
            print(1)
    elif 'size' in l :
        print(len(q))
    elif 'pop' in l :
        if q:
            print(q.popleft())
        else:
            print(-1)