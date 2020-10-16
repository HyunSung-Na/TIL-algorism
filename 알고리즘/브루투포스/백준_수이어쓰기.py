n = int(input())

result = 0
start = 1
length = 1

while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    result += (end - start + 1) * length
    start *= 10
    length += 1

print(result)