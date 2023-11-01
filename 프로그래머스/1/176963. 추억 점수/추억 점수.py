def solution(name, yearning, photo):
    answer = []

    for i in photo:
        cnt = 0
        for j in name:
            if j in i:
                ni = name.index(j)
                yi = yearning[ni]

                cnt += yi
        answer.append(cnt)

    return answer