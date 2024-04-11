import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline().rstrip())

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                count += 1
    print(count)