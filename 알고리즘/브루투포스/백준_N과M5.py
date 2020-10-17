n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
check = [False for x in range(n + 1)]
result = []

def combine(index, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        result.append(array[i])
        combine(index + 1, n, m)
        check[i] = False
        result.pop()


combine(0, n, m)
