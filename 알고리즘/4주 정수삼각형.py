def solution(triangle):
    answer = 0
    N = len(triangle)
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for index1 in range(2, N+1):
        for index2 in range(1, index1+1):
            DP[index1][index2] = max(DP[index1-1][index2-1], DP[index1-1][index2]) + triangle[index1][index2]

    for index in DP:
        print(index)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))