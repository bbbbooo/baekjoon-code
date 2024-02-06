import sys
import math


def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


n, k = map(int, sys.stdin.readline().rstrip().split())
print(int(binomial_coefficient(n, k)))
