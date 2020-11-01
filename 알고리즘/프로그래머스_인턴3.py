import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
num = 0

def solution(v):
    global num

    answer = []
    n = len(v)
    for i in range(n):
        for j in range(n):
            dfs(i, j, n, answer, v)
            answer.append(num)
    return answer


def dfs(nx, ny, n, answer, v):
    global num

    visited = [[0] * n for _ in range(n)]
    visited[nx][ny] = 1


    for j in range(4):
        next_x = nx + dx[j]
        next_y = ny + dy[j]
        if visitable(n, nx, ny, next_x, next_y, visited, v):
            dfs(next_x, next_y, n, answer, v)


def visitable(n, nx, ny, next_x, next_y, visit, v):
    return 0 <= next_x < n and 0 <= next_y < n and not visit[nx][ny] and v[nx][ny] == v[next_x][next_y]

v = [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]
print(solution(v))