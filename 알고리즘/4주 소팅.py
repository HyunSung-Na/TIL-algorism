def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        if budget >= money:
            budget -= money
            answer += 1
    return answer

d = [1, 3, 2, 5, 4]
budget = 6

print(solution(d, budget))