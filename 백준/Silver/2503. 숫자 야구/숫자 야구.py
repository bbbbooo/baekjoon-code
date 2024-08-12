n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 가능한 모든 세 자리 수를 탐색 (a, b, c는 서로 다른 숫자여야 함)
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue

            cnt = 0
            for arr in hint:
                number = str(arr[0])
                expected_strike = arr[1]
                expected_ball = arr[2]

                # 현재 숫자 조합
                current = str(a) + str(b) + str(c)

                strike_count = 0
                ball_count = 0

                # 스트라이크 계산
                for i in range(3):
                    if current[i] == number[i]:
                        strike_count += 1

                # 볼 계산 (숫자는 존재하나 위치가 다름)
                for i in range(3):
                    if current[i] in number and current[i] != number[i]:
                        ball_count += 1

                # 현재 힌트와 일치하면 cnt 증가
                if strike_count == expected_strike and ball_count == expected_ball:
                    cnt += 1

            # 모든 힌트에 대해 일치하는 경우 정답으로 인정
            if cnt == n:
                answer += 1

print(answer)
