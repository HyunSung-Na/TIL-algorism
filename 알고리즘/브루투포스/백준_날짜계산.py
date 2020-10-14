E, S, M = map(int, input().split())

E -= 1
S -= 1
M -= 1
num = 0

while True:
    if num % 15 == E and num % 28 == S and num % 19 == M:
        print(num + 1)
        break
    num += 1

