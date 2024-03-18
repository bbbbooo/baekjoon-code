def solution(clothes):
    dict = {}

    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1

        else :
            dict[i[1]] = 1

    answer = 1
    for type in dict:
        answer *= (dict[type] + 1)

    return answer - 1