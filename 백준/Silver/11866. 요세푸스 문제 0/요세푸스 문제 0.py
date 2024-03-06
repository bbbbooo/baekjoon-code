import sys

n, k = map(int, sys.stdin.readline().split())
index = 0
l = []
array = list(range(1, n+1))

while len(array) != 0 :
    index += (k-1)
    index %= len(array)
    l.append(array.pop(index))

print("<", end="")
for i in range(n -1):
    print(l[i], end=", ")
print(l[n - 1], end="")
print(">", end="")