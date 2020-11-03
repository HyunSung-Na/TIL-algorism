from collections import deque

N, M, x, y, K = list(map(int, input().split()))

array = []
dice = [0] * 7

for _ in range(N):
    array.append(list(map(int, input().split())))

move = list(map(int, input().split()))

queue = deque(move)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    next_point = queue.popleft() - 1
    nx = x + dx[next_point]
    ny = y + dy[next_point]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    if next_point == 0:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif next_point == 1:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif next_point == 2:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp

    x = nx
    y = ny

    if not array[x][y]:
        array[x][y] = dice[6]
    else:
        dice[6] = array[x][y]
        array[x][y] = 0

    print(dice[1])