N, M = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
checked = [False for _ in range(N + 1)]


for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


for g in graph:
    g.sort()

component = 0


def dfs(start):
    checked[start] = True
    for j in range(len(graph[start])):
        z = graph[start][j]
        if not checked[z]:
            dfs(z)

for i in range(1, N + 1):
    if not checked[i]:
        dfs(i)
        component += 1

print(component)