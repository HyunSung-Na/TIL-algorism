from collections import deque

n = int(input())
house = []
for _ in range(n):
    water = input().strip().split(' ')
    house.append(list(water))

water_place = [0, 0]
hong_place = [n-1, n-1]

def bfs(n, m, x, y, house, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy

            if visitable(n, m, next_x, next_y, visited) and house[next_x][next_y] == house[x][y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

visited = [[True for x in range(n)] for x in range(n)]


