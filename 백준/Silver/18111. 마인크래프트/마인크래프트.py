import sys

n, m, b = map(int, sys.stdin.readline().rstrip().split())
field = []
answer = sys.maxsize
idx = 0

for i in range(n):
    q = list(map(int, sys.stdin.readline().rstrip().split()))
    field.append(q)

for floor in range(257):
    over, lack = 0, 0

    for i in range(n):
        for j in range(m):
            if field[i][j] > floor:
                over += field[i][j] - floor
            else:
                lack += floor - field[i][j]

    if over + b >= lack:
        if (over * 2) + lack <= answer:
            answer = (over * 2) + lack
            idx = floor

print(answer, idx)