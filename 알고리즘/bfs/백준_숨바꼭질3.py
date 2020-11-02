from collections import deque

N, K = map(int, input().split())

queue = deque([N])
MAX = 100001
memory = [-1] * MAX
memory[N] = 0

while queue:
    x = queue.popleft()
    for next_x in [2 * x, x + 1, x - 1]:
        if 0 <= next_x < MAX and memory[next_x] == -1:
            if next_x == 2 * x:
                queue.appendleft(next_x)
                memory[next_x] = memory[x]
            else:
                queue.append(next_x)
                memory[next_x] = memory[x] + 1

print(memory[K])