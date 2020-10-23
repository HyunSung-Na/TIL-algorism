n = int(input())

operator = input().split()
check = [False for x in range(10)]
result = []


def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True


def operation(index, num):

    global result

    if index == n + 1:
        result.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), operator[index-1]):
            check[i] = True
            operation(index + 1, num + str(i))
            check[i] = False

operation(0, '')
print(result[-1])
print(result[0])
