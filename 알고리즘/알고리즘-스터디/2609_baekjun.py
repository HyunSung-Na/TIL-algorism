A, B = list(map(int, input().split(' ')))
a, b = A, B

while not b:
    a = a % b
    a, b = b, a

print(a)

print(A * B // a)

