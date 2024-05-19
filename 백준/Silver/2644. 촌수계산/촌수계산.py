import sys
from collections import deque
sys.setrecursionlimit(30000)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            dfs(i)

dfs(a)
print(visited[b] if visited[b] > 0 else -1)