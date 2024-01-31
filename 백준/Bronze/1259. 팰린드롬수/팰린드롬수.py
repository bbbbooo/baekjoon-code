import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    ns = str(n)
    nl = list(ns)

    nl.reverse()
    nr = ''.join(nl)
    
    if ns == nr:
        print('yes')
    else :
        print('no')
