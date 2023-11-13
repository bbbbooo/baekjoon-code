import sys

n, p = map(int, sys.stdin.readline().strip().split())
s = [[] for _ in range(7)]
cnt = 0

for _ in range(n):
    line, fret = map(int, sys.stdin.readline().strip().split())

    while s[line] and s[line][-1] > fret:
        s[line].pop()
        cnt += 1

    if not s[line] or s[line][-1] < fret:
        s[line].append(fret)
        cnt += 1

print(cnt)
