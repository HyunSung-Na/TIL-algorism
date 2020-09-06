x = 20000
food_list = [100, 1500, 1200, 300]

def solution(x, food_list):
    food_list.sort(reverse=True)
    index = 0
    result = 0
    while x:
        if food_list[index] <= x:
            x -= food_list[index]
            result += 1
        elif index < len(food_list) - 1:
            index += 1
        else:
            if food_list[index] > x:
                x -= food_list[index]
                result += 1
                break
    return result

print(solution(x, food_list))

N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

def solution1(N, M, V, edges):

    adj = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(M):
        a, b = edges[i]
        adj[a][b] = 1
        adj[b][a] = 1

    def dfs(start):
        start -= 1
        visited = []
        stack = edges[start]
        while stack:
            current_node = stack[0]
            next_node = stack[1]
            if current_node not in visited:
                visited.append(current_node)
                if adj[current_node][next_node]:
                    stack = edges[next_node]
                if next_node >= N:
                    visited.append(next_node)
                    break
            start += 1
            stack = edges[start]
        return " ".join(str(i) for i in visited)
    print(dfs(V))

solution1(N, M, V, edges)


from collections import deque

def solution3(N, M, V, edges):

    adj = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for i in range(M):
        a, b = edges[i]
        adj[a][b] = 1
        adj[b][a] = 1

    def bfs(start):
        start -= 1
        queue = deque(edges)
        visited = []
        while queue:
            n = queue.popleft()
            current_node = n[0]
            next_node = n[1]
            if current_node not in visited:
                visited.append(current_node)
            if n == edges[-1]:
                visited.append(next_node)
                break
        return " ".join(str(i) for i in visited)

    print(bfs(V))

solution3(N, M, V, edges)

import heapq

a = {'A': {'B': 2, 'C': 5, 'D': 1}, 'B': {'C': 8}, 'C': {}, 'D': {'C': 3}}
start = 'A'
final = 'C'

def solution4(a, start, final):
    distances = {node: float('inf') for node in a}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in a[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    result = distances[final]
    return result

print(solution4(a, start, final))