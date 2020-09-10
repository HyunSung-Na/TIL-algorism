def number_insert(triangle, num):
    number = 1
    height = 0
    width = 0
    cicle = 0
    while cicle < num:
        if height < num and width < num and cicle < num:
            for i in range(num - cicle):
                if not triangle[height][width]:
                    triangle[height][width] = number
                    number += 1
                height += 1
            cicle += 1
            height -= 1
            width += 1
            for i in range(num - cicle):
                if not triangle[height][width]:
                    triangle[height][width] = number
                    number += 1
                width += 1
            cicle += 1
            width -= 1
            for i in range(num - cicle):
                height -= 1
                width -= 1
                if not triangle[height][width]:
                    triangle[height][width] = number
                    number += 1
    return triangle

def solution(n):
    answer = []
    triangle = []
    for i in range(1, n + 1):
        triangle.append([0] * i)
    for i in number_insert(triangle, n):
        answer.extend(i)
    return answer

print(solution(4))