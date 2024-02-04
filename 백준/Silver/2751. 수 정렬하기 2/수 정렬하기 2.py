import sys

n = int(sys.stdin.readline().rstrip())

l = []
for _ in range(n):
    num = l.append(int(sys.stdin.readline().rstrip()))
l.sort()

for i in l:
    print(i)