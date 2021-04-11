n = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
result = 0

for i in stick:
    if n >= i:
        result += 1
        n -= i

    if not n:
        break

print(result)

