def solution(s):
    answer = True
    stack = []
    for s_String in s:
        if s_String == "(":
            stack.append(s_String)
        elif s_String == "[":
            stack.append(s_String)
        elif s_String == "{":
            stack.append(s_String)
        else:
            if not stack:
                answer = False
                break
            if s_String == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    answer = False
                    break
            elif s_String == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    answer = False
                    break
            elif s_String == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    answer = False
                    break
    if stack:
        answer = False
    return answer
