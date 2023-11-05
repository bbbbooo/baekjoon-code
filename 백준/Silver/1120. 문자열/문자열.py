import sys

a, b = map(str, sys.stdin.readline().strip().split())
minr = len(a)

for i in range(len(b)-len(a)+1) :
    result = 0
    
    for j in range(len(a)):
        if a[j] != b[i+j]:
            result +=1
        if result > minr:
            break
    minr = min(minr, result)

print(minr)