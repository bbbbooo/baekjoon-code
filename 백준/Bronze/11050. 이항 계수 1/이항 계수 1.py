import sys
import itertools


def binomial_coefficient(n, k):
    combinations = list(itertools.combinations(range(n), k))
    return len(combinations)


n, k = map(int, sys.stdin.readline().rstrip().split())
print(binomial_coefficient(n, k))
