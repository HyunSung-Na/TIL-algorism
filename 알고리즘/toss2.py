user_input = input().split(" ")

def lotto(user_input):
    user_input = list(map(int, user_input))
    user_sort = sorted(user_input)
    user_set = set(user_input)
    USER_NUMBER = [x for x in range(1, 46)]
    print(user_input, user_set, user_sort)
    if len(user_set) != len(user_input):
        return "false"
    if user_sort != user_input:
        return "false"
    for user in user_input:
        if user not in USER_NUMBER:
            return "false"

    return "true"

print(lotto(user_input))
