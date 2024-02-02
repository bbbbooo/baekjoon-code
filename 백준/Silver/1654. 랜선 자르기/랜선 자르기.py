import sys

k, n = map(int, sys.stdin.readline().rstrip().split())
l = []
for _ in range(k):
    l.append(int(sys.stdin.readline().rstrip()))
l.sort()
s = 1
e = max(l)

while s <= e:
    mid = (s+e)//2
    lan = 0

    for i in l:
        lan += i//mid

    if lan >= n :
        s = mid+1
    else:
        e = mid-1

print(e)