from collections import deque

user_input = input().split(" ")
user_memory = deque()

def memory_input(user_input):
    for user in user_input:
        if not len(user_memory):
            user_memory.append(user)
        if len(user_memory) > 5:
            user_memory.popleft()
        if user not in user_memory:
            user_memory.appendleft(user)
        elif user in user_memory:
            user_memory.remove(user)
            user_memory.appendleft(user)
        print(*[x for x in user_memory])

memory_input(user_input)


