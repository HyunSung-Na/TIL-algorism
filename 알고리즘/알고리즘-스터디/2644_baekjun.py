from collections import deque

N = int(input())

person1, person2 = list(map(int, input().split(' ')))

relation_num = int(input())

relation_map = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = 0

for _ in range(relation_num):
    p, m = list(map(int, input().split(' ')))
    relation_map[p].append(m)
    relation_map[m].append(p)


def bfs(v, target):
    count = 0

    queue = deque([[v, count]])

    while queue:
        value = queue.popleft()
        v = value[0]
        count = value[1]
        if v == target:
            return count

        if not visited[v]:
            count += 1
            visited[v] = True
            for node in relation_map[v]:
                if not visited[node]:
                    queue.append([node, count])
    return -1

print(bfs(person1, person2))
