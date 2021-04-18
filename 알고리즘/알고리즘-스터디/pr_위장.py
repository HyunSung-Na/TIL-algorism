import itertools


def solution(clothes):
    answer = 0
    dic_clothes = dict(clothes)
    result = []

    for i in range(1, len(clothes) + 1):
        product = itertools.combinations(dic_clothes, i)
        for p in product:
            flag = True
            key_dic = []
            for e in range(len(p)):
                if dic_clothes[p[e]] in key_dic:
                    flag = False
                    break
                key_dic.append(dic_clothes[p[e]])
            if flag:
                answer += 1
                result.append(p)
    return answer

from collections import defaultdict

def solution1(clothes):
    answer = 1

    dict_clothes = defaultdict(lambda: 0)

    for key, value in clothes:
        dict_clothes[value] += 1

    count_kind = [x for x in dict_clothes.values()]

    for num in count_kind:
        answer *= num + 1

    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution1(clothes))