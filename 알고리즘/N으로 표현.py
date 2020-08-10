def right_num(N, number):
    while int(N) // 10 != number // 10:
        N += str(N)
    return N
def dfs(N, number):
    stack = []
    if N == number:
        return 1
    N = right_num(N, number)

    return N

def solution(N, number):
    answer = 0
    print(dfs(N, number))
    return answer

N = 5
number = 12
print(solution(N, number))