import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

l = []
for i in range(n):
    k = int(sys.stdin.readline().rstrip())
    l.append(k)


def average(l):
    return round(sum(l) / n)


def middle(l):
    l.sort()
    return l[len(l) // 2]


def many(l):
    cnt = Counter(l).most_common(2)

    if len(l) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else :
            return cnt[0][0]
    else:
        return cnt[0][0]


def range(l):
    l.sort()
    return max(l) - min(l)

sys.stdout.write(str(average(l)) + '\n')
sys.stdout.write(str(middle(l)) + '\n')
sys.stdout.write(str(many(l)) + '\n')
sys.stdout.write(str(range(l)) + '\n')