n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()
result = []

def combine(index, start, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n):
        result.append(array[i])
        combine(index + 1, i + 1, n, m)
        result.pop()


combine(0, 0, n, m)