def solution(s):
    answer = True
    stack = []
    PAIRS = {")": "(", "}": "{", "]": "["}
    for bracket in s:
        if bracket in PAIRS.values():
            stack.append(bracket)
        else:
            if not stack:
                answer = False
                break
            if bracket in PAIRS.keys():
                if stack[-1] == PAIRS.get(bracket):
                    stack.pop()
                else:
                    answer = False
                    break

    if stack:
        answer = False
    return answer