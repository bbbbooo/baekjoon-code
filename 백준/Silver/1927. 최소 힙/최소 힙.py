import sys
import heapq

n = int(sys.stdin.readline().strip())
h = []

for i in range(n):
    x = int(sys.stdin.readline().strip())

    if x == 0 and not h:
        print(0)

    elif x == 0:
        result = heapq.heappop(h)
        print(result)

    else:
        heapq.heappush(h, x)