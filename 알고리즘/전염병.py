from collections import deque

def bfs(n, m, x, y, infests, vaccinateds, visited):
    queue = deque()
    empty = m * n
    count = 0
    for vaccinated in vaccinateds:
        a, b = vaccinated
        visited[a - 1][b - 1] = True
        empty -= 1

    for infest in infests:
        a, b = infest
        visited[a - 1][b - 1] = True
        empty -= 1
        queue.append([a - 1, b - 1, 0])

    while queue and empty:
        print(x,y)
        x, y = queue.popleft()
        visited[x][y] = True
        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            if visitable(n, m, next_x, next_y, visited) and infest[next_x][next_y] == infest[x][y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                empty -= 1
                count += 1
    return count if empty >= 0 else -1
def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def solution(m, n, infests, vaccinateds):
    answer = 0
    visited = [[[False] for _ in range(n)] for _ in range(m)]


    for index1 in range(m):
        for index2 in range(n):
            answer = bfs(m, n, index1, index2, infests, vaccinateds, visited)

    return answer


m = 2
n = 4
infests = [[1,4],[2,2]]
vaccinateds = [[1,2]]
print(solution(m,n,infests,vaccinateds))