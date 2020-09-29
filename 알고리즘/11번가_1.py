def solution(S):
    answer = 0
    stack = []
    for word in S:
        if word == 'a':
            stack.append(word)
        else:
            if len(stack) < 2:
                while len(stack) < 2:
                    answer += 1
                    stack.append('a')
                stack = []
            else:
                stack = []
        if len(stack) >= 3:
            return -1
    if S[-1] != 'a':
        answer += 2
    return answer

S = "dog"
print(solution(S))