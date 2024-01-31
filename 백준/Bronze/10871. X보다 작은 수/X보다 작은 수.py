import sys

n,x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
r = []
for i in l:
    if i < x:
        r.append(i)

print(' '.join(map(str, r)))

