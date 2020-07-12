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

def solution(nums):
    answer = 0
    num_combines = combinations(nums, 3)
    nums_sum = sum(nums)
    prime_num = Prime(nums_sum)
    for num in num_combines:
        if sum(num) in prime_num:
            answer += 1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))