n, m = map(int, input().split())

result = []

def combine(index, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        result.append(i)
        combine(index + 1, n, m)
        result.pop()


combine(0, n, m)
