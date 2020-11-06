from collections import deque

N = int(input())
K = int(input())

checked = deque()
board = [[0] * N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 1

for _ in range(K):
    x, y = list(map(int, input().split()))
    board[x-1][y-1] = 1

L = int(input())

info = {}

for _ in range(L):
    second, way = input().split()
    info[int(second)] = way
x, y = 0, 0
direction = 1


def change(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

board[0][0] = 2
checked.append([0, 0])

while True:
    x = x + dx[direction]
    y = y + dy[direction]

    if 0 <= x < N and 0 <= y < N and [y, x] not in checked:
        if board[y][x] != 1:
            temp_y, temp_x = checked.popleft()
            board[temp_y][temp_x] = 0

        board[y][x] = 2
        checked.append([y, x])

        if result in info.keys():
            direction = change(direction, info[result])
        result += 1
    else:
        break

print(result)