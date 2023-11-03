from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(i,p) for i,p in enumerate(priorities)])

    while q:
        current = q.popleft()
        if any(current[1] < priority[1] for priority in q):
            q.append(current)
        else:
            answer += 1
            if current[0] == location:
                break

    return answer