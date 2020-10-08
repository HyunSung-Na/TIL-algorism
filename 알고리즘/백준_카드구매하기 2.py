n = int(input())
P = [0] + list(map(int, input().split()))

dp = [False for _ in range(len(P))]
for i in range(1, n + 1):
    for j in range(i + 1):
        if not dp[i]:
            dp[i] = dp[i - j] + P[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + P[j])

print(dp[n])