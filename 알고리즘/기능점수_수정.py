from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speed = deque(speeds)
    while queue:
        for index in range(len(queue)):
            queue[index] += speed[index]

        count = 0
        while queue and queue[0] >= 100:
            queue.popleft()
            speed.popleft()
            count += 1
        if count:
            answer.append(count)
    return answer