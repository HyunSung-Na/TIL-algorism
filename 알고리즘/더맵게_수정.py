import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] <= K:
        min_scovfirst = heapq.heappop(scoville)
        if scoville:
            min_scovsecond = heapq.heappop(scoville)
            new_food = min_scovfirst + (min_scovsecond * 2)
        else:
            return -1
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer

scoville = [1]
K = 3
print(solution(scoville,K))