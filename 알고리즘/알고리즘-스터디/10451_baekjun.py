test_case = int(input())


def check(m):
    checked[m] = True
    if not checked[array[m - 1]]:
        check(array[m - 1])

for index in range(test_case):
    N = int(input())
    array = list(map(int, input().split(' ')))

    checked = [False for x in range(N + 1)]
    count = 0

    for i in range(1, N + 1):
        if not checked[i]:
            checked[i] = True
            count += 1
            if not checked[array[i - 1]]:
                check(array[i - 1])

    print(count)

