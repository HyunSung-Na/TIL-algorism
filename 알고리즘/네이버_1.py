def solution(n, p, c):
    notSumit = 0
    ball = 0
    total = 0
    for day in range(n):
        if p[day] + ball >= c[day]:
            if notSumit:
                if notSumit == 1:
                    total += c[day] * 50
                    notSumit = 0
                elif notSumit == 2:
                    total += c[day] * 25
                    notSumit = 0
            else:
                total += c[day] * 100
            ball = (p[day] + ball) - c[day]
        else:
            ball += p[day]
            notSumit += 1
            if notSumit > 2:
                answer = str('%.2f' % (total / (day + 1)))
                return answer
    answer = str('%.2f' % (total / n))
    return answer


n = 6
p = [5, 4, 7, 2, 0, 6]
c = [4, 6, 4, 9, 2, 3]

n1 = 7
p1 = [6, 2, 1, 0, 2, 4, 3]
c1 = [3, 6, 6, 2, 3, 7, 6]

print(solution(n, p, c))