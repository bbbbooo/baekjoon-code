import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            three = l[i] + l[j] + l[k]
            if three > m:
                continue
            else:
                cnt.append(three)
print(max(cnt))