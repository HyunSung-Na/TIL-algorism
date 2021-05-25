from collections import deque

num = int(input())

for _ in range(num):
    N, M = list(map(int, input().split(' ')))
    queue = deque()
    number_list = []
    for i, v in enumerate(list(map(int, input().split(' ')))):
        queue.append([i, v])
        number_list.append(v)

    number_list.sort()
    count = 1
    first = number_list.pop()

    while queue:
        i, v = queue.popleft()
        if v == first:
            if i == M:
                print(count)
                break
            else:
                first = number_list.pop()
            count += 1
        else:
            queue.append([i, v])
