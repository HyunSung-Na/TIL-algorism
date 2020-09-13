from collections import deque

def solution(ball, order):
    answer = []
    queue = deque(ball)
    order = deque(order)
    while queue:
        first_ball = queue[0]
        last_ball = queue[-1]
        for index in range(len(order)):
            orderball = order[index]
            if orderball == first_ball:
                queue.popleft()
                answer.append(orderball)
                break
            elif orderball == last_ball:
                queue.pop()
                answer.append(orderball)
                break
    return answer

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

print(solution(ball, order))