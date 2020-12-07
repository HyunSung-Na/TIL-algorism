import heapq


def solution(votes):
    votes = list(votes)
    queue = []
    hero = votes.pop(0)
    result = 0

    if not votes:
        return 0

    for i in votes:
        heapq.heappush(queue, i)

    while queue[-1] >= hero:
        result += 1
        hero += 1
        queue[-1] -= 1
        print(queue)
        heapq.heapify(queue)

    return result

votes = [5, 10, 7, 3, 8]
print(solution(votes))