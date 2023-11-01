import sys
from collections import deque

seq = int(sys.stdin.readline())

for _ in range(seq) :
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0

    l = deque(list(map(int, sys.stdin.readline().split())))

    while True:
        maxn = max(l)
        temp = l.popleft()

        if temp < maxn:
            l.append(temp)

        else:
            cnt +=1
            if m == 0:
                print(cnt)
                break

        m -=1
        if m <0 :
            m = len(l) -1