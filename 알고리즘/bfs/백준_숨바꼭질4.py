from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            p = []
            while x != n:
                p.append(x)
                x = path[x]
            p.append(n)
            p.reverse()
            print(' '.join(map(str, p)))
            return
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                path[nx] = x
                q.append(nx)

MAX = 100000
n, k = map(int, input().split())
dist = [0]*(MAX+1)
path = [0]*(MAX+1)
bfs()