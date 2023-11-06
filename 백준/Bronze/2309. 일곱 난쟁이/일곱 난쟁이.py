import sys

a=0
b=0
l = []
for i in range(9) :
    l.append(int(sys.stdin.readline().strip()))


sum = sum(l)
for i in range(8) :
    for j in range(1+i, 9) :
        if sum - (l[i]+l[j]) == 100:
            a = l[i]
            b = l[j]

l.remove(a)
l.remove(b)
l.sort()

for i in l:
    print(i)