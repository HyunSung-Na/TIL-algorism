def solution(A):
    answer = 0
    A.sort()
    while A[0] != 1:
        if A[0] > 1:
            A[0] -= 1
            answer += 1
        else:
            A[0] += 1
            answer += 1
    for index in range(1, len(A)):
        if A[index] == A[index - 1] + 1:
            continue
        else:
            if A[index] <= A[index - 1]:
                while A[index] <= A[index - 1]:
                    A[index] += 1
                    answer += 1
            else:
                while A[index] != A[index - 1] + 1:
                    A[index] -= 1
                    answer += 1
    return answer

A = [6, 2, 3, 5, 6, 3]
print(solution(A))