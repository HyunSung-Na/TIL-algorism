def solution(land):
    N = len(land)
    for index in range(0, N - 1):
        land[index + 1][0] += max(land[index][1], land[index][2], land[index][3])
        land[index + 1][1] += max(land[index][0], land[index][2], land[index][3])
        land[index + 1][2] += max(land[index][0], land[index][1], land[index][3])
        land[index + 1][3] += max(land[index][0], land[index][1], land[index][2])
    answer = max(land[N - 1])
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))