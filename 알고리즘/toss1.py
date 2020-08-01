user_input = input()
stack = []

def number_right(user_input):
    number_boolean = "true"
    for user in user_input:
        if len(stack) == 0:
            stack.append(user)
        if stack[-1] == '1':
            if user == '1':
                number_boolean = "false"
                return number_boolean
            else:
                stack.append(user)
        else:
            stack.append(user)
    if len(stack) > 0 and number_boolean == "true":
        return number_boolean

print(number_right(user_input))