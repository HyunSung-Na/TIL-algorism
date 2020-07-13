from itertools import combinations

def solution(m, weights):
    answer = 0
    for candys in range(1, len(weights)):
        totals = map(sum, combinations(weights, candys))
        for total in totals:
            if total == m:
                answer += 1
    return answer

m = 3000
weights = [500, 1500, 2500, 1000, 2000]
print(solution(m, weights))