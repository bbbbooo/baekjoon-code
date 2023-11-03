import sys

n, m = map(int, sys.stdin.readline().strip().split())
s = set()
l = []

for i in range(n):
    s.add(sys.stdin.readline().strip())

for i in range(m):
    name = sys.stdin.readline().strip()
    if name in s:
        l.append(name)

l.sort()
print(len(l))
for name in l:
    print(name)


