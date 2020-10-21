def solution(sum_num, goal):
    if sum_num > goal:
        return 0
    if sum_num == goal:
        return 1
    return solution(sum_num + 1, goal) + solution(sum_num + 2, goal) + solution(sum_num + 3, goal)

n = int(input())

for i in range(n):
    goal = int(input())
    print(solution(0, goal))

