import sys

while True:
    n = sys.stdin.readline().rstrip()
    s = []
    odd = 1
    for i in n:
        if i == '[' or i == '(':
            s.append(i)

        elif i == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                odd = 0
                break
        elif i == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                odd = 0
                break
    if n == '.':
        break

    if not s and odd:
        print('yes')
    else :
        print('no')