def solution(goods):
    goods = list(goods)
    goods.sort()
    if sum(goods) < 50:
        return sum(goods)

    if goods[0] >= 50:
        return sum(goods) - 30

    elif goods[1] >= 50:
        return sum(goods) - 20

    elif goods[2] >= 50:
        if goods[0] + goods[1] >= 50:
            return sum(goods) - 20
        else:
            return sum(goods) - 10
    else:
        if sum(goods) >= 50:
            return sum(goods) - 10
        else:
            return sum(goods)
    return 0


class Solution:
    pass


good = [30, 50, 10]

print(solution(good))
