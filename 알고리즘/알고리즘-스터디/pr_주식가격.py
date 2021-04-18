def solution(prices):
    N = len(prices)
    answer = [0 for _ in range(N)]
    stack = []

    for i in range(N):
        while stack and prices[i] < prices[stack[len(stack) - 1]]:
            temp = stack.pop()
            answer[temp] = i - temp

        stack.append(i)

    while stack:
        temp = stack.pop()
        answer[temp] = N - temp - 1

    return answer

prices = [1, 2, 3, 2, 3]

print(solution(prices))
