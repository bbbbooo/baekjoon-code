import sys

n = int(sys.stdin.readline().rstrip())
l = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    l.append((x, y))

sl = sorted(l, key = lambda x:(x[1], x[0]))

for i in sl:
    x, y = i
    print(x, y)