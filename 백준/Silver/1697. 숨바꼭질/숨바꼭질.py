from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

max = 100000
visited = [0] * (max+1)

def bfs(s):
    queue = deque([s])
    visited[s] = 0

    while queue:
        current = queue.popleft()
        if current == k:
            return visited[k]

        for i in (current - 1, current + 1, current * 2):
            if 0 <= i <= max and not visited[i]:
                visited[i] = visited[current] + 1
                queue.append(i)


print(bfs(n))
