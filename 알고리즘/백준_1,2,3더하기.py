n = int(input())
input_list = []
for _ in range(n):
    input_list.append(int(input()))

dp = [1, 1, 2, 4]

for i in range(4, max(input_list) + 1):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]))

for i in input_list:
    print(dp[i])