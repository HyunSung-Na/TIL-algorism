from itertools import combinations


def isPrime(number):
    if number < 2:
        return False
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True


def Prime(n):
    prime_num = []
    for num in range(n):
        if isPrime(num):
            prime_num.append(num)
    return prime_num


def solution(n):
    answer = 0
    num_list = Prime(n)
    num_sums = list(combinations(num_list, 3))
    for num_sum in num_sums:
        if sum(num_sum) == n:
            answer += 1
    return answer

n = 33
print(solution(n))