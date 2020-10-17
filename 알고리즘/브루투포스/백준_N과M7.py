n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

result = []

def combine(index, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(array[i])
        combine(index + 1, n, m)
        result.pop()


combine(0, n, m)
