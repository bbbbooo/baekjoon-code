import sys

n = int(sys.stdin.readline().strip())
l = []

for i in range(n):
    w = sys.stdin.readline().strip()

    if w not in l:
        l.append(w)

l.sort()
l.sort(key=len)

for i in l:
    print(i)