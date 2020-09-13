orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

import itertools
from collections import deque

def solution(orders, course):
    answer = []
    result = []
    queue = deque(orders)
    while queue:
        i_menu = queue.popleft()
        menus = []
        count = len(queue)
        for couse in course:
            menus.append(itertools.combinations(i_menu, couse))
        for menu in menus:
            for i in menu:
                while count:
                    count -= 1
                    temp = ''.join(i)
                    for tem in temp:
                        if tem in queue[count]:
                            result += tem
                    if len(result) == len(temp):
                        answer.append(''.join(result))
                    result = []
                count = len(queue)
    result = set(answer)
    return sorted(list(result))

print(solution(orders, course))