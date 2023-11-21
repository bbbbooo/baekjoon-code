def solution(phone_book):
    h = set(phone_book)

    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num

            if temp in h and temp != phone:
                return False

    return True