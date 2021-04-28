N = int(input())
street = list(input())
max_num = 9999999
dp = [max_num] * N
dp[0] = 0


def prev_position(x):
    if x == 'B':
        return 'J'
    elif x == 'O':
        return 'B'
    elif x == 'J':
        return 'O'

for i in range(1, N):
    prev = prev_position(street[i])

    for j in range(i):
        if street[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

print(dp[N - 1] if dp[N - 1] != max_num else -1)
