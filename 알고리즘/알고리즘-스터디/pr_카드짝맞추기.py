import queue

import math

Board = []
All_card = {}
All_removed = 1
Min_count = math.inf
D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(removed, src, dst):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = queue.Queue()
    q.put(src)
    while q:
        curr = q.get()
        if curr[0] == dst[0] and curr[1] == dst[1]:
            return curr[2]

        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]

            if nr < 0 or nr > 3 or nc < 0 or nc > 3:
                continue

            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.put((nr, nc, curr[2] + 1))

            for j in range(2):
                if (removed & 1 << Board[nr][nc]) == 0:
                    break
                if nr + D[i][0] < 0 or nr + D[i][0] > 3 \
                        or nc + D[i][1] < 0 or nc + D[i][1] > 3:
                    break

                nr += D[i][0]
                nc += D[i][1]
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.put((nr, nc, curr[2] + 1))
    return math.inf


def permutate(cnt, removed, src):
    global Min_count

    if cnt >= Min_count:
        return

    if removed == All_removed:
        Min_count = min(Min_count, cnt)
        return

    for num, card in All_card.items():
        if removed & 1 << num:
            continue

        one = bfs(removed, src, card[0]) + bfs(removed, card[0], card[1]) + 2
        two = bfs(removed, src, card[1]) + bfs(removed, card[1], card[0]) + 2

        permutate(cnt + one, removed | 1 << num, card[1])
        permutate(cnt + two, removed | 1 << num, card[0])


def solution(board, r, c):
    global Board, All_card, All_removed
    Board = board

    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            if num:
                All_removed |= 1 << num
                if num in All_card:
                    All_card[num].append((i, j, 0))
                else:
                    All_card[num] = [(i, j, 0)]

    permutate(0, 1, (r, c, 0))
    return Min_count


board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0

print(solution(board, r, c))
