n = int(input())

graph = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
nums = 0

for i in range(n):
    graph[i].extend(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def visitable(n, nx, ny, visit, metrix):
    return 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and metrix[nx][ny]


def dfs(x, y, c):

    global nums

    visited[x][y] = 1
    if graph[x][y] == 1:
        graph[x][y] = c
        nums += 1

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if visitable(n, nx, ny, visited, graph):
            dfs(nx, ny, c)

cnt = 1
numlist = []

for k in range(n):
    for p in range(n):
        if graph[k][p] and not visited[k][p]:
            dfs(k, p, cnt)
            numlist.append(nums)
            nums = 0
            cnt += 1

print(len(numlist))

for num in sorted(numlist):
    print(num)