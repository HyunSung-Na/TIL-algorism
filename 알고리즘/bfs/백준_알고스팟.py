from collections import deque

N, M = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

array = []
visited = [[-1] * N for _ in range(M)]

for _ in range(M):
    array.append(list(map(int, list(input()))))

queue = deque()
visited[0][0] = 0
queue.append([0, 0])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == -1:
            if not array[nx][ny]:
                queue.appendleft([nx, ny])
                visited[nx][ny] = visited[x][y]
            elif array[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

print(visited[M-1][N-1])

