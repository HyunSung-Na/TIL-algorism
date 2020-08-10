from itertools import product

def list_move(S):
    stack = []
    for num in range(1, S+1):
        stack.append(num)
    return stack

def solution(monster, S1, S2, S3):
    range_move = S1 + S2 + S3 + 2
    place = set([(m - 1) for m in monster if m <= range_move])
    result = 0
    first_move = list_move(S1)
    secend_move = list_move(S2)
    third_move = list_move(S3)
    move_list = [first_move, secend_move, third_move]
    move = product(*move_list)
    for move_case in move:
        if sum(move_case) in place:
            result += 1
    return int((1 - result / S1 / S2 / S3) * 1000)

monster = [4, 9, 5, 8]
S1 = 2
S2 = 3
S3 = 4

print(solution(monster, S1, S2, S3))