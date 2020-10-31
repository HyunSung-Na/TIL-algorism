from collections import deque

S = int(input())

MAX_NUM = 1001

array = [[-1] * MAX_NUM for _ in range(MAX_NUM)]
answer = -1
queue = deque()

array[1][0] = 0
queue.append([1, 0])

while queue:
    s, c = queue.popleft()
    if array[s][s] == -1:
        array[s][s] = array[s][c] + 1
        queue.append([s, s])

    if array[s + c][c] == -1 and s + c <= S:
        array[s + c][c] = array[s][c] + 1
        queue.append([s + c, c])

    if array[s - 1][c] == -1 and s - 1 >= 0:
        array[s - 1][c] = array[s][c] + 1
        array.append([s-1, c])

for i in range(S):
    if array[S][i] != -1:
        if answer == -1 or answer > array[S][i]:
            answer = array[S][i]

print(answer)
