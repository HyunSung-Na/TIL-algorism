def solution(arrangement):
    answer = 0
    stack = []

    for index, stick in enumerate(arrangement):
        if stick == '(':
            stack.append([stick,index])
        else:
           if stack[-1][-1]+1 == index:
                stack.pop()
                answer += len(stack)
           else:
                stack.pop()
                answer += 1
    return answer

arrangement = "()(((()())(())()))(())"
print(solution(arrangement))