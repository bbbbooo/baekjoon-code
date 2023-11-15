import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

all = permutations(a)
ans = 0

for i in all:
    s = 0
    for j in range(1, n):
        s += abs(i[j] - i[j - 1])
    if ans < s:
        ans = s
print(ans)