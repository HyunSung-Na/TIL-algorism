n, m = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
for i in range(1, (1 << n)):
    num_sum = 0
    for k in range(n):
        if i & (1 << k):
            num_sum += numbers[k]

    if num_sum == m:
        result += 1

print(result)