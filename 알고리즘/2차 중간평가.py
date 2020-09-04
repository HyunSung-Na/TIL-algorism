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
        visited = []
        stack = edges[start]

        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                if n in edges:
                    temp = list(set(edges[n]) - set(visited))
                    temp.sort(reverse=True)
                    stack += temp
            return " ".join(str(i) for i in visited)
    print(dfs(V))

solution1(N, M, V, edges)


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