def set_check(Arrays):
    stack = []
    for array in Arrays:
        if array not in stack:
            stack.append(array)
    return stack

def sum_set(ArrayA, ArrayB):
    stack = []
    for array in ArrayA:
        for index in range(len(ArrayB)):
            if array != ArrayB[index] and array not in stack:
                stack.append(array)
    return stack

def desSet(ArrayA, ArrayB):
    stack = []
    for array in ArrayA:
        if array not in ArrayB and array not in stack:
            stack.append(array)
    return stack

def intersection(ArrayA, ArrayB):
    stack = []
    for array in ArrayA:
        if array in ArrayB:
            stack.append(array)
    return stack

def solution(ArrayA, ArrayB):
    set_A = set_check(ArrayA)
    set_B = set_check(ArrayB)
    insum = sum_set(set_A, set_B)
    des = desSet(set_A, set_B)
    inter = intersection(set_A, set_B)
    answer = [len(set_A), len(set_B), len(insum), len(des), len(inter)]
    return answer

ArrayA = [1,2,3,2]
ArrayB = [1,3]
print(solution(ArrayA, ArrayB))