import sys

n, m = map(int, sys.stdin.readline().split())
route = [[0 for i in range(n)] for j in range(m)]
visited = [[False for i in range(n)] for j in range(m)]

dx = [1, 0]
dy = [0, 1]

for i in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    route[i] = l


def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        if x == m - 1 and y == n - 1:
            return True

        if not visited[x][y]:
            visited[x][y] = True

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or route[nx][ny] == 0:
                continue

            if not visited[nx][ny]:
                stack.append((nx, ny))
    return False



if dfs(0, 0):
    print('Yes')
else:
    print('No')
