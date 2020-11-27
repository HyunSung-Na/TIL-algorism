import random


def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    return quicksort(left) + [pivot] + quicksort(right)

data_list = random.sample(range(100), 10)
data_qsort = quicksort(data_list)
print(data_qsort)
