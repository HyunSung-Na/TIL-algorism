
N, M, K = list(map(int, input().split(' ')))

combination = [' '] * (N + M)
p = N + M
char_list = ['a', 'z']
count = 0

def go(n, m, index):

    if not n:
        for b in range(index, p):
            combination[b] = 'z'
        print(''.join(combination))
        return
    if not m:
        for a in range(index, p):
            combination[a] = 'a'
        print(''.join(combination))
        return

    if index == p:
        print(''.join(combination))
        return

    for j in range(2):
        combination[index] = char_list[j]
        if not j:
            go(n - 1, m, index + 1)
        else:
            go(n, m - 1, index + 1)

go(N, M, 0)