number = input()

a, b, c = 0, 0, 0

if len(number) == 1:
    print(number)
    exit()
elif len(number) == 2:
    b = int(number[0]) * 3
    c = int(number[1]) * 1
elif len(number) == 3:
    a = int(number[0]) * 1
    b = int(number[1]) * 3
    c = int(number[2]) * 1

d = a + b + c

while len(str(d)) != 1:

    num = str(d)
    numbers = []

    for n in num:
        numbers.append(n)
    numbers = map(int, numbers)
    d = sum(numbers)

print(d)