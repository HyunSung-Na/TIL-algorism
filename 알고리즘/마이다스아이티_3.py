import itertools


def solution(cookies, k):
    x = len(cookies)
    dp = [1 for i in range(x)]
    result = []
    for i in range(x):
        for j in range(i):
            if cookies[i] > cookies[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_cook = max(dp)

    combine = itertools.combinations(cookies, max_cook)
    for com in combine:
        if sorted(com) == list(com):
            result.append(list(com))
    answer = sorted(result)[k - 1]
    return answer

cookies = [1, 4, 2, 6, 5, 3]
k = 2
print(solution(cookies, k))
