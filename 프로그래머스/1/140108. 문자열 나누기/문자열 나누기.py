def solution(s):
    answer = 1
    x = s[0]
    x_count = other_count = 0

    for i in range(len(s) - 1):
        if s[i] == x:
            x_count += 1
        else:
            other_count += 1

        if x_count >= 1 and x_count == other_count:
            answer += 1
            x = s[i + 1]
            x_count = other_count = 0

    return answer