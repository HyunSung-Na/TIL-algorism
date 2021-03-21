test_case = int(input())

for _ in range(test_case):
    N = int(input())

    count_zero = 1
    count_one = 0

    for _ in range(N):
        count_zero, count_one = count_one, count_zero
        count_one += count_zero

    print(count_zero, count_one)

