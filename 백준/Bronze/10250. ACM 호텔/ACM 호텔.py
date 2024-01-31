import sys

t = int(sys.stdin.readline())
for i in range(t):
    h,w,n = map(int, sys.stdin.readline().split())

    num = n//h+1
    floor = n%h

    if floor == 0:
        num = n//h
        floor = h

    print(floor*100+num)



