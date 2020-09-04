def solution(n, lost, reserve):
    answer = n
    student = [False for x in range(n + 1)]
    for lent in reserve:
        student[lent] = True
    for cloth in lost:
        if student[cloth]:
            student[cloth] = False
        elif cloth != n and student[cloth + 1]:
            student[cloth + 1] = False
        elif cloth != 0 and student[cloth - 1]:
            student[cloth - 1] = False
        else:
            answer -= 1
    return answer


n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))