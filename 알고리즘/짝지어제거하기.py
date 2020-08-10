def solution(s):
    answer = 0
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        answer = 1
    return answer

