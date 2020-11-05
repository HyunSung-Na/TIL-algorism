dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def change(d):
    if not d:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def find(r, c, d):
    cnt = 1
    x = r
    y = c
    arr[x][y] = 2 
    while True:
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]

            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                cnt += 1
                x = nx
                y = ny
                arr[nx][ny] = 2
                d = dc
                empty = 1
                break

        if not empty:
            if not d:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            if arr[x][y] == 1:
                break
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = find(r, c, d)
print(res)
