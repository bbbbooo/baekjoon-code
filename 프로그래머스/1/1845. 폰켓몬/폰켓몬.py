def solution(nums):
    u = len(set(nums))

    if len(nums)/2 > u:
        return u
    else:
        return len(nums)/2