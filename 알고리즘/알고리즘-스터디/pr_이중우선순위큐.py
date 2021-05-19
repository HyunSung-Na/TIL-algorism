import heapq


def solution(operations):
    answer = []
    max_heap = []
    min_heap = []

    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    for operation in operations:
        oper_split = operation.split(' ')

        if oper_split[0] == 'I':
            heapq.heappush(min_heap, int(oper_split[1]))
            heapq.heappush(max_heap, -int(oper_split[1]))
        elif oper_split[0] == 'D':
            if oper_split[1] == '1':
                if max_heap:
                    heapq.heappop(max_heap)
            elif oper_split[1] == '-1':
                if min_heap:
                    heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        return [0, 0]

    for heap_value in max_heap:
        temp = -heap_value
        if temp in min_heap and temp not in answer:
            answer.append(temp)

    if len(answer) < 2:
        return [0, 0]

    answer.sort()
    return [answer[-1], answer[0]]