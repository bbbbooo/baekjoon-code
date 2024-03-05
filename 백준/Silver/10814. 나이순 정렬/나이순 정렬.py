import sys

n = int(sys.stdin.readline())
d = []
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    d.append((a, b))

d.sort(key= lambda x : x[0])

for i in d:
    print(i[0], i[1])
