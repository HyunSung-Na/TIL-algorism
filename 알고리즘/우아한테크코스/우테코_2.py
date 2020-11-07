def calculation(front, end, op):
    if op == '+':
        return front + end
    elif op == '-':
        return front - end
    elif op == '*':
        return front * end


def solution(s, op):
    answer = []
    number_of_cases = len(list(s))
    for index in range(1, number_of_cases):
        front = int(s[:index])
        end = int(s[index:])
        answer.append(calculation(front, end, op))
    return answer

s = "987987"
op = "-"

print(solution(s, op))