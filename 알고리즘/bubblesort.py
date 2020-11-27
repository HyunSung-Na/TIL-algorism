import random


def bubbliest(data):
    for index in range(len(data)):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True

        if not swap:
            break

    return data

data_list = random.sample(range(100), 50)
bubbliest(data_list)
print(data_list)