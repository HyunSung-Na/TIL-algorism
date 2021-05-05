import sys

N, M = list(map(int, sys.stdin.readline().split()))

array = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[0] = array[0]

for i in range(1, len(array)):
    dp[i] = dp[i - 1] + array[i]

for _ in range(M):
    x, y = list(map(int, sys.stdin.readline().split()))

    if x == 1:
        print(dp[y-1])
        continue
    else:
        print(dp[y-1] - dp[x-2])
        continue
