import itertools

k = 5

def solution(k):
    answer = 0
    numbers = [[6, 0], [2, 1], [5, 2], [5, 3], [4, 4], [5, 5], [6, 6], [3, 7], [7, 8], [6, 9]]
    numbers_sort = sorted(numbers)
    first_result = []
    result = []
    if k < 2:
        return answer
    for number_sort in numbers_sort:
        if k == number_sort[0]:
            first_result.append(number_sort)
    while k >= 2:
        for number_sort in numbers_sort:
            if k >= number_sort[0]:
                k -= number_sort[0]
                result.append(number_sort)
    product = itertools.combinations(result, 2)
    for pro in product:
        if sum(pro) == 5:
            first_result.append(sum(pro))
    print(result, first_result)
    answer = len(result) + len(first_result)
    return answer

print(solution(k))