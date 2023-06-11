n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)

for i in range(len(l)):
    l[i] -= (i + 1 - 1)
    if l[i] < 0:
        l[i] = 0

print(sum(l))
