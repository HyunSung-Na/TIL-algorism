import itertools

N = int(input())
array = list(map(int, input().split(' ')))
operate = list(map(int, input().split(' ')))

plus = operate[0] * ['+']
minus = operate[1] * ['-']
double = operate[2] * ['*']
half = operate[3] * ['/']

op_list = plus + minus + double + half
permutation = itertools.permutations(op_list, len(op_list))
op_list = list(set(permutation))


def operations(num, num1, oper):
    if oper == '+':
        return num + num1
    elif oper == '-':
        return num - num1
    elif oper == '*':
        return num * num1
    else:
        if num < 0:
            return -(-num // num1)
        else:
            return num // num1

max_num = -99999999
min_num = 99999999

for oper in op_list:
    result = array[0]

    for i in range(N - 1):
        result = operations(result, array[i + 1], oper[i])

    max_num = max(max_num, result)
    min_num = min(min_num, result)

print(max_num)
print(min_num)