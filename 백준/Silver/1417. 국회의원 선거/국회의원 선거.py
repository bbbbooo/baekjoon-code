import sys
import heapq

n = int(sys.stdin.readline().rstrip())
dasom = int(sys.stdin.readline().rstrip())

heap = []
queue = heapq

for i in range(n - 1):
    m = int(sys.stdin.readline().rstrip())
    queue.heappush(heap, (-m, m))

if len(heap) == 0:
    print(0)

else:
    count = 0
    while True:
        now = queue.heappop(heap)[1]
        if now >= dasom:
            count += 1
            dasom += 1
            heapq.heappush(heap, (-now + 1, now - 1))
        else:
            break
    print(count)