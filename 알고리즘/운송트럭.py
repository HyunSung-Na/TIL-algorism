def solution(max_weight, specs, names):
    answer = 1
    items = dict(specs)
    weight = 0
    for name in names:
        weight += int(items.get(name))
        if max_weight < weight:
            answer += 1
            weight = int(items.get(name))
    return answer