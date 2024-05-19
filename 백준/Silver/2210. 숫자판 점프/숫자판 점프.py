import sys
from collections import deque

board = [["" for _ in range(5)] for _ in range(5)]
result = set()

for i in range(5):
    board[i] = list(map(str, sys.stdin.readline().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.add(number)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        else:
            dfs(nx, ny, number + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(result))