def mid_value(budgets, mid):
    stack_min = []
    stack_max = []
    for budget in budgets:
        if budget <= mid:
            stack_min.append(budget)
        else:
            stack_max.append(budget)
    min = sum(stack_min)
    max = sum(stack_max)
    return [min,max,len(stack_max)]


def solution(budgets, M):
    budgets.sort()
    for budget in budgets:
        if budget * len(budgets) <= M:
            mid_budget = budget
    if sum(budgets) <= M:
        return max(budgets)
    sumlist = mid_value(budgets, mid_budget)
    remainder = M - sumlist[0]
    notEnough = remainder - (sumlist[2] * mid_budget)
    answer = (notEnough // sumlist[2]) + mid_budget
    return answer

budgets = [10, 20, 30]
M = 55

print(solution(budgets, M))