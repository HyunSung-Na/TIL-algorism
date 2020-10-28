N = int(input())


def dfs(start, c):
    checked[start] = c
    for j in range(len(graph[start])):
        z = graph[start][j]
        if not checked[z]:
            dfs(z, 3-c)

for _ in range(N):
    V, E = list(map(int, input().split()))
    graph = [[] for _ in range(V + 1)]
    checked = [0 for _ in range(V + 1)]

    for _ in range(E):
        x, y = list(map(int, input().split()))
        graph[x].append(y)
        graph[y].append(x)

    for g in graph:
        g.sort()

    for i in range(1, V + 1):
        if not checked[i]:
            dfs(i, 1)

    ok = True

    for k in range(1, V + 1):
        for p in range(len(graph[k])):
            w = graph[k][p]
            if checked[k] == checked[w]:
                ok = False

    print("YES" if ok else "NO")
