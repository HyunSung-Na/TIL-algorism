user_input = list(map(str, input().split(' ')))
s = '(()[[]])([])'


def solution(user_input):
    stack = [[], []]
    first = 2
    second = 3
    sum_stack = 0

    for i in user_input:
        if i == '(' or i == '[':
            stack.append(i)