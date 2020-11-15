def solution(openA, closeB):
    answer = 0
    last_time = closeB[-1]
    flag = False
    openA.sort(reverse=True)
    closeB.sort(reverse=True)
    next_open = openA.pop()
    next_close = closeB.pop()
    for i in range(1, last_time + 1):

        if flag:
            answer += 1

        if i == next_open:
            flag = True
            if openA:
                next_open = openA.pop()
            else:
                next_open = -1
        elif i == next_close:
            flag = False
            if closeB:
                next_close = closeB.pop()
    return answer

openA = [4, 7, 9, 16]
closeB = [2, 5, 12, 14, 20]

print(solution(openA, closeB))