n = int(input())
array = [[0] * n for _ in range(n)]
b = list(input())
v, k = [], 0


def possible(index):
    s = 0
    for t in range(index, -1, -1):
        s += v[t]
        if array[t][index] == '+' and s <= 0:
            return False
        if array[t][index] == '0' and s != 0:
            return False
        if array[t][index] == '-' and s >= 0:
            return False
    return True


def solve(index):
    if index == n:
        print(' '.join(map(str, v)))
        exit(0)
    for h in range(-10, 11):
        v.append(h)
        if possible(index):
            solve(index + 1)
        v.pop()


for i in range(n):
    for j in range(i, n):
        array[i][j] = b[k]
        k += 1
solve(0)
