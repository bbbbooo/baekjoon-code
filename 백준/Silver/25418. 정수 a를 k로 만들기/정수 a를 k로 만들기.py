import sys
from collections import deque

a, k = map(int, sys.stdin.readline().split())

def bfs(a, k):
    if a == k :
        return 0

    visited = set()
    queue = deque([(a, 0)])

    while queue:
        current, distance = queue.popleft()
        next = [current + 1, current * 2]

        for next_node in next:
            if next_node == k:
                return distance + 1

            if next_node not in visited and next_node <= k:
                visited.add(next_node)
                queue.append((next_node, distance + 1))

    return -1

count = bfs(a, k)
print(count)
