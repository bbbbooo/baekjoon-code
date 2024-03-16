import sys

n = int(sys.stdin.readline().rstrip())
l = []
wanted = []
average = 0

def myRound(param):
    if param - int(param) >= 0.5: # 
        return int(param)+1
    else :
        return int(param)

if n == 0:
    print(0)
else :
    average = myRound(n * 15 / 100)
    for i in range(n):
        l.append(int(sys.stdin.readline().rstrip()))

    l.sort()
    if average > 0 :
        wanted = l[average:-average]
        result = sum(l[average:-average])
        print(myRound(result / len(wanted)))
    else:
        print(myRound(sum(l) / len(l)))
