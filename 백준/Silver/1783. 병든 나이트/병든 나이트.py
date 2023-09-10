from sys import stdin

n, m = map(int, stdin.readline().split())

if n == 1:  # 행이 1이면 이동불가
    print(1)
elif n == 2:  # 행이 2면 2,3번만 사용가능
    print(min(4, (m+1)//2))
else:  # 행이 3이상

    if m < 7:  
        print(min(4, m))
    else: 
        print(m-2)