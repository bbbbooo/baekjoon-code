import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
answer = 0

for i in range(l):
    no = ord(s[i]) - 96
    answer += (no * (31 ** i))

print(answer)