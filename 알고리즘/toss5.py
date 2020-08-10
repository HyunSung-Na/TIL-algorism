user_input_kim = list(map(int,input().split(" ")))
user_input_lee = list(map(int,input().split(" ")))

def payment(kim, lee):
    sum_pay = 0
    stack = []
    for index in range(len(kim)):
        sum_pay += kim[index] - lee[index]
        print(sum_pay)
        if kim[index] <= lee[index]:
            stack.append(0)
        else:
            if sum_pay > 0:
                stack.append(sum_pay)
    return print(*stack)
payment(user_input_kim, user_input_lee)
