N = int(input())
A = list(map(int, input().split(' ')))
B, C = list(map(int, input().split(' ')))

result = 0

for student in A:
    num = student
    if num <= B:
        result += 1
    else:
        num -= B
        result += 1
        while num > 0:
            num -= C
            result += 1

print(result)