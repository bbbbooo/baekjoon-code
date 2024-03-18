import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    a,b = 1,0
    for i in range(n):
        a, b = b, a+b
    print(a,b)