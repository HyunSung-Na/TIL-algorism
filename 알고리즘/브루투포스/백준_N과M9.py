n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
check = [False for x in range(n)]
result = []

def combine(index, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return

    temp = 0
    for i in range(n):
        if not check[i] and temp != array[i]:
            check[i] = True
            result.append(array[i])
            temp = array[i]
            combine(index + 1, n, m)
            check[i] = False
            result.pop()


combine(0, n, m)
