def solution(binomial):
    l = binomial.split()

    a = int(l[0])
    op = l[1]
    b = int(l[2])

    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

