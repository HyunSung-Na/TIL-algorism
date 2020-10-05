N = int(input())

dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if not i % 2:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if not i % 3:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
