matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

def searchMatrix(data, target):
    matrix = []
    for num_list in data:
        matrix.extend(num_list)
    matrix.sort()
    start = 0
    end = len(matrix) - 1

    while start <= end:
        mid = (start + end) // 2

        if matrix[mid] == target:
            return True
        elif matrix[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

print(searchMatrix(matrix, 11))


A = 'ababababab'
B = 'abab'

def gcdString(A, B):
    list_a = list(A)
    list_b = list(B)
    result = []
    len_index = 0
    max_index = 0
    if len(list_a) > len(list_b):
        len_index = len(list_b)
        max_index = len(list_a)
    else:
        len_index = len(list_a)
        max_index = len(list_b)
    for index in range(len_index):
        if list_a[0] != list_b[0]:
            return result
        if list_a[index] == list_b[index]:
            result.append(list_a[index])

    while max_index % len(result):
        result.pop()

    return ''.join(result)

print(gcdString(A, B))

from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer


class Solution(object):
    def findJudge(self, N, trust):
        graph = {i: [] for i in range(1, N + 1)}
        for t in trust:
            graph[t[0]].append(t[1])

        for k in graph:
            if len(graph[k]) == 0:
                judge = k
                for person in graph:
                    if person != judge and judge not in graph[person]:
                        return -1
                return judge

        return -1