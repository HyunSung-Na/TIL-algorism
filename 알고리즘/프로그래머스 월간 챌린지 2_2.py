def quad_tree(x, y, n):
    global one, zero, array
    color = array[y][x]
    double_break = False

    for i in range(x, x + n):
        if double_break:
            break

        for j in range(y, y + n):
            if array[j][i] != color:
                quad_tree(x, y, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                double_break = True
                break

    if not double_break:
        if array[y][x] == 1:
            one += 1
        else:
            zero += 1
    print(zero, one)
    return [zero, one]


def solution(arr):
    n = len(arr)
    globals(arr)
    answer = quad_tree(0, 0, n)
    return answer

def globals(arr):
    global array
    array = arr
array = []
one, zero = 0, 0
arra = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]

print(solution(arra))
