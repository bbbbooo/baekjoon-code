import sys

n = int(sys.stdin.readline().strip())
stack = []

plus ='+'
minus = '-'

result = []
current = 1

for i in range(n) :
    m = int(sys.stdin.readline().strip())

    while current <= m:
        stack.append(current)
        result.append(plus)
        current +=1

    if not stack or stack[-1] != m:
        print('NO')
        exit(0)

    stack.pop()
    result.append(minus)

print('\n'.join(result))