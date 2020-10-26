from collections import deque

N, M, V = list(map(int, input().split()))

checked = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
result = []

for i in range(M):
    k, p = list(map(int, input().split()))
    graph[k].append(p)
    graph[p].append(k)

for g in graph:
    g.sort()


def dfs(start):
    checked[start] = True
    result.append(start)
    for j in range(len(graph[start])):
        y = graph[start][j]
        if not checked[y]:
            dfs(y)

dfs(V)
print(*result)
result = []
checked = [False for _ in range(N + 1)]
queue = deque()


def bfs(st):
    checked[st] = True
    queue.append(st)
    result.append(st)
    while queue:
        x = queue.popleft()
        for index in range(len(graph[x])):
            next_node = graph[x][index]
            if not checked[next_node]:
                checked[next_node] = True
                queue.append(next_node)
                result.append(next_node)

bfs(V)
print(*result)
