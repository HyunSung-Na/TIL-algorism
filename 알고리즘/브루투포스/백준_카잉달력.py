t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    ok = False
    for i in range(x, n * m, m):
        if i % n == y:
            print(i + 1)
            ok = True
            break
    if not ok:
        print(-1)


