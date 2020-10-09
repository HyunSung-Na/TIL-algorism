n = int(input())

array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
index = dp.index(max_dp)
result = []

while index >= 0:
    if dp[index] == max_dp:
        result.append(array[index])
        max_dp -= 1
    index -= 1

print(max(dp))
print(*sorted(result))