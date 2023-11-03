import sys

n = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

stack = []

for i in n:
    stack.append(i)
    if ''.join(stack[-len(b):]) == b:
        del stack[-len(b):]

result = ''.join(stack)

if len(result) == 0:
    print('FRULA')
else:
    print(result)
