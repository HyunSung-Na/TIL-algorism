n, m = map(int, input().split())

result = []

def combine(index, start, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n + 1):
        result.append(i)
        combine(index + 1, i, n, m)
        result.pop()


combine(0, 1, n, m)