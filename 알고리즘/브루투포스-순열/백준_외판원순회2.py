from itertools import permutations

n = int(input())

W = []

for i in range(n):
    array = list(map(int, input().split()))
    W.append(array)

result = 10000000

index = [i for i in range(n)]

def solution(r):
    global W, n
    temp = 0
    for i in range(len(r) - 1):
        if W[r[i]][r[i+1]] != 0:
            temp += W[r[i]][r[i+1]]
        else:
            return -1

    if W[r[-1]][r[0]] != 0:
        temp += W[r[-1]][r[0]]
    else:
        return -1

    return temp

for num in permutations(index):
    per = solution(num)
    if per != -1:
        result = min(result, per)

print(result)