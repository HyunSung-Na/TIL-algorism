n = int(input())

dp = [[0 for i in range(10)] for j in range(101)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, 101):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= 1000000000
        if j + 1 <= 9:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] %= 1000000000

print(sum(dp[n]) % 1000000000)