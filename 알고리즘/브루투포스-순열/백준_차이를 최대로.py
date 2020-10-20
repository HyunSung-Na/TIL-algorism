from itertools import permutations

n = int(input())

num_list = permutations(list(map(int, input().split())))

answer = 0

for nums in num_list:
    sum_nums = 0
    for i in range(n - 1):
        sum_nums += abs(nums[i] - nums[i - 1])
    answer = max(answer, sum_nums)

print(answer)