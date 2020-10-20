import itertools

n = int(input())
nums = []

for i in range(1, n + 1):
    nums.append(i)

combine = itertools.permutations(nums, n)

for num in combine:
    print(*num)