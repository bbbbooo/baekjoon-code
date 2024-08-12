a, b, c, d, e, f = map(int, input().split()) # 1 3 -1 4 1 7

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if a*x + b*y == c:
            if d*x + e*y == f:
                print(x, y)