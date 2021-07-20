import itertools


def solution(n, k):
    list_num = [x for x in range(1, n + 1)]
    combine = itertools.permutations(list_num)
    result = []
    for com in combine:
        k -= 1
        if k == 0:
            result.extend(list(com))
    return result


n, k = 3 , 3
print(solution(n, k))



