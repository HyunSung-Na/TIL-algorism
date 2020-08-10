def dfs(computers, visited, start):
    network = [start]
    while network:
        next_com = network.pop()
        if visited[next_com] == 0:
            visited[next_com] = 1
        for index in range(0, len(computers)):
            if computers[network][index] == 1 and visited[index] == 0:
                network.append(index)


def solution(n, computers):
    answer = 0
    visited = [0] * n
    start = 0
    while 0 in visited:
        if visited[start] == 0:
            dfs(computers, visited, start)
            answer += 1
        start += 1
    return answer