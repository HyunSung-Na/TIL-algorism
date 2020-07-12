import math
from collections import deque

def minus_num(v, l):
    queue = deque(v)
    result = []
    if len(queue) < 2:
        result.append(queue[0])
        result.append(l - queue[0])
        return result
    temp1 = queue.popleft()
    temp2 = queue.popleft()
    result.append(temp1)
    while queue:
        minus = temp2 - temp1
        result.append(minus)
        temp1 = temp2
        temp2 = queue.popleft()
    result.append(temp2 - temp1)
    result.append(l - temp2)
    return result

def solution(l, v):
    v.sort()
    nums = minus_num(v, l)
    if len(nums) < 2:
        answer = max(nums)
        return answer
    print(nums)
    num_max = max(nums)
    if num_max == nums[0] or num_max == nums[-1]:
        answer = num_max
    else:
        num = num_max / 2
        answer= math.ceil(num)
    return answer

v = [15,5,3,7,9,14,0]
l = 15

print(solution(l, v))