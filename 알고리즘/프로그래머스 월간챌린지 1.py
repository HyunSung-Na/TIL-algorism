from itertools import combinations

numbers = [2, 1, 3, 4, 1]

def solution(numbers):
    answer = []
    combin_number = combinations(numbers, 2)
    for num1, num2 in combin_number:
        answer.append(num1 + num2)
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(numbers))