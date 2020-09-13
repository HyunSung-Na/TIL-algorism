from collections import deque
import collections

def solution(boxes):
    answer = 0
    result = deque()
    for box in boxes:
        result.extend(box)
    nums = list(set(result))
    set_num = [0 for x in range(nums[-1] + 1)]
    while result:
        num = result.popleft()
        set_num[num] += 1
    count = collections.Counter(set_num)
    remain_box = len(boxes) - count[2]
    remain_item = count[1]
    while remain_box:
        if remain_item:
            answer += 1
            remain_box -= 1
            remain_item -= 1
    return answer


boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]

print(solution(boxes))