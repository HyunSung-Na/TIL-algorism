from collections import deque


def solution(n, delivery):
    success = list()
    result = [0] * (n + 1)
    queue = deque(delivery)
    while queue:
       item1, item2, deliver = queue.popleft()
       if deliver:
           if item1 not in success:
                success.append(item1)
           if item2 not in success:
                success.append(item2)
    success.sort()
    queue = deque(delivery)
    while queue:
        item1, item2, deliver = queue.popleft()
        if deliver:
            result[item1] = 'O'
            result[item2] = 'O'
            continue
        else:
            if item1 in success:
                result[item2] = 'X'
            elif item2 in success:
                result[item1] = 'X'
            else:
                if not result[item1]:
                    result[item1] = '?'
                if not result[item2]:
                    result[item2] = '?'
    for i in range(len(result)):
        if not result[i]:
            result[i] = '?'
    re = deque(result)
    re.popleft()
    answer = ''.join(re)
    return answer

n = 6
delivery = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]
print(solution(n, delivery))