
def visitable(n, m, nx, ny, visit, metrix):
    return 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and metrix[nx][ny]


def dfs(nx, ny):

    visited[nx][ny] = 1

    for j in range(8):
        next_x = nx + dx[j]
        next_y = ny + dy[j]

        if visitable(x, y, next_x, next_y, visited, island):
            dfs(next_x, next_y)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:

    x, y = list(map(int, input().split()))

    if not x and not y:
        break

    island = [[] for _ in range(y)]

    visited = [[0]*x for _ in range(y)]

    land_num = 0

    for i in range(y):
        island[i].extend(list(map(int, input().split())))

    for k in range(y):
        for p in range(x):
            if island[k][p] and not visited[k][p]:
                dfs(k, p)
                land_num += 1

    print(land_num)


