from collections import deque

def solution(n):
    answer = ''
    watermelon = deque()
    watermelon.append("수")
    watermelon.append("박")
    for index in range(n):
        temp = watermelon.popleft()
        answer += temp
        watermelon.append(temp)
    return answer

print(solution(5))