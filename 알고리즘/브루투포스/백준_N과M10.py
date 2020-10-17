n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
check = [False for x in range(n)]
result = []

def combine(index, start, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return

    temp = 0
    for i in range(start, n):
        if not check[i] and temp != array[i]:
            check[i] = True
            result.append(array[i])
            combine(index + 1, i + 1, n, m)
            temp = array[i]
            check[i] = False
            result.pop()


combine(0, 0, n, m)
