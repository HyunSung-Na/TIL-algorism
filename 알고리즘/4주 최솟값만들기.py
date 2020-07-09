def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for index in range(len(A)):
        answer += A[index] * B[index]
    return answer

A = [1, 4, 2]
B = [5, 4, 4]

print(solution(A, B))