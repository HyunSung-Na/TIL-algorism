from collections import deque

N, M = list(map(int, input().split(' ')))

board = [list(input()) for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
blue, red = 0, 0


def bfs(red, blue):
    queue = deque([(red, blue)])
    visited = {(red, blue)}
    result = 0

    while queue and result <= 10:
        size = len(queue)

        for _ in range(size):
            red, blue = queue.popleft()

            if board[red[0]][red[1]] == 'O':
                return result

            for dx, dy in zip(dxs, dys):
                is_possible = True

                next_ball = [-1, -1]
                ball_step = [0, 0]
                for ball_idx, ball in enumerate([red, blue]):
                    x, y = ball
                    nx, ny = x + dx, y + dy
                    while True:
                        if board[nx][ny] == '.':
                            x, y = nx, ny
                            nx, ny = nx + dx, ny + dy
                            ball_step[ball_idx] += 1
                            continue
                        elif board[nx][ny] == 'O':
                            if ball == blue:
                                is_possible = False
                            else:
                                x, y = nx, ny
                                ball_step[ball_idx] += 1
                            break
                        else:
                            break
                    next_ball[ball_idx] = (x, y)

                if next_ball[0] == next_ball[1]:
                    if ball_step[0] < ball_step[1]:
                        a, b = next_ball[1]
                        next_ball[1] = (a - dx, b - dy)
                    else:
                        a, b = next_ball[0]
                        next_ball[0] = (a - dx, b - dy)
                next_ball = tuple(next_ball)
                if is_possible and next_ball not in visited:
                    queue.append(next_ball)
                    visited.add(next_ball)
        result += 1

    return -1

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'

        elif board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'


print(bfs(red, blue))
