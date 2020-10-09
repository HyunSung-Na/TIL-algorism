n = int(input())

array = list(map(int, input().split()))

dp = [0 for _ in range(len(array))]

for i in range(n):
    dp[i] = array[i]
    if not i:
        continue
    if dp[i] < dp[i - 1] + array[i]:
        dp[i] = dp[i - 1] + array[i]

print(max(dp))