def solution(no, works):
    result = 0
    while no > 0:
        works.sort(reverse=True)
        if works[0] > 0:
            works[0] -= 1
            no -= 1
    for i in works:
        result += i*i
    return result

a = [4,3,3]
print(solution(4,a))