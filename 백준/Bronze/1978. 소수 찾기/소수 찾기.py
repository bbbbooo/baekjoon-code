import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for num in l:
    if num < 2:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        cnt +=1

print(cnt)