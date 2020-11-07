from collections import deque


def move(x, y, n):

    result = []

    for index in range(4):
        next_x = x + dx[index]
        next_y = y + dy[index]

        if next_x < 0:
            next_x += n
        elif next_x >= n:
            next_x -= n

        if next_y < 0:
            next_y += n
        elif next_y >= n:
            next_y -= n

        result.append([next_x, next_y])

    return result

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solution(n, board):
    answer = 0
    x, y = 0, 0
    dp = [[0] * n for _ in range(n)]
    move_count = 0
    for num in range(1, n**2 + 1):
        queue = deque(move(x, y, n))

        while queue:
            next_x, next_y = queue.popleft()
            move_count += 1

            if board[next_x][next_y] == num:
                board[next_x][next_y] = 0
                move_count += 1
                dp[next_x][next_y] += 1
            else:
                queue.extend(move(next_x, next_y, n))
    return answer

board = [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
n = 3

print(solution(n, board))