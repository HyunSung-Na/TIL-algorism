from collections import deque

n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

result = []


def bfs(x_start, y_start, x_end, y_end):
    q = deque()
    q.append([x_start, y_start])
    checked[x_start][y_start] = 1
    while q:
        k, p = q.popleft()
        if k == x_end and p == y_end:
            return checked[k][p] - 1
        for i in range(8):
            nx = k + dx[i]
            ny = p + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if checked[nx][ny] == 0:
                    q.append([nx, ny])
                    checked[nx][ny] = checked[k][p] + 1

for _ in range(n):
    size = int(input())
    x, y = list(map(int, input().split()))
    goal_x, goal_y = list(map(int, input().split()))
    checked = [[0] * size for _ in range(size)]
    if x == goal_x and y == goal_y:
        print(0)
        continue

    answer = bfs(x, y, goal_x, goal_y)
    print(answer)

