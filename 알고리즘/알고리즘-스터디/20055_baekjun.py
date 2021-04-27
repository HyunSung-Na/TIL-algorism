from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)

result = 0

while belt.count(0) < K:
    belt.rotate(1)
    robot.rotate(1)

    robot[-1] = 0

    if sum(robot):
        for idx in range(N - 2, -1, -1):
            if robot[idx] and not robot[idx + 1] and belt[idx + 1]:
                belt[idx + 1] -= 1
                robot[idx + 1], robot[idx] = 1, 0

        robot[-1] = 0

    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1

    result += 1

print(result)
