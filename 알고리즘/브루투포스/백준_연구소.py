from collections import deque

N, M = map(int, input().split())

board = []
visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    board.append(list(map(int, input().split())))

