n = int(input())


def is_balanced(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


for _ in range(n):
    expression = input()
    if is_balanced(expression):
        print("YES")
    else:
        print("NO")
