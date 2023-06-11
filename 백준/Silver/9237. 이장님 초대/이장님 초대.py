n = int(input())
b = list(map(int, input().split()))
b.sort(reverse=True)

for i in range(n):
    b[i] += i

result = max(b)+2
print(result)