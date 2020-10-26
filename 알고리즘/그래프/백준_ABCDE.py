n, m = list(map(int, input().split()))

checked = [[False for x in range(m + 1)] for y in range(n + 1)]
near_list = [[] for z in range(n)]
edges = []

for i in range(m):
    j, k = list(map(int, input().split()))
    edges.append([j, k])
    edges.append([k, j])
    checked[j][k], checked[k][j] = True, True
    near_list[j].append(k)
    near_list[k].append(j)

m *= 2

for p in range(m):
    for u in range(m):
        A = edges[p][0]
        B = edges[p][1]

        C = edges[u][0]
        D = edges[u][1]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not checked[B][C]:
            continue
        for E in near_list[D]:
            if A == E or B == E or C == E or D == E:
                continue

            print(1)
            exit()
print(0)