import heapq

def solution(no, works):
    if no > sum(works):
        return 0
    works = [(-heap_work, heap_work) for heap_work in works]
    heapq.heapify(works)
    for _ in range(no):
        work = heapq.heappop(works)[1] - 1
        print(work)
        heapq.heappush(works, (-work, work))
    return sum([result[1]**2 for result in works])

print(solution(3,[4,3,3]))