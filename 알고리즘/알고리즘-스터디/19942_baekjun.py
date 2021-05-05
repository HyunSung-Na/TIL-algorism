
def passOrNot(v, usedIdx):
    global mn
    for i in range(4):
        if req[i] > v[i]:
            return False
    mn = v[4]
    mnIdx.clear()
    mnIdx.extend(usedIdx)
    return


def DFS(L, v, usedIdx):
    global mn
    if v[4] >= mn:
        return
    if passOrNot(v, usedIdx):
        return
    if L == n:
        return
    else:
        usedIdx.append(L+1)
        for i in range(5):
            v[i] += data[L][i]
        DFS(L + 1, v, usedIdx)

        usedIdx.pop()
        for i in range(5):
            v[i] -= data[L][i]
        DFS(L + 1, v, usedIdx)

if __name__ =='__main__':
    n = int(input())
    req = list(map(int, input().split()))
    data = [list(map(int, input().split())) for i in range(n)]
    mn = 9999999
    mnIdx = []
    DFS(0, [0] * 5, [])

    if mn == 9999999:
        print(-1)
    else:
        print(mn)
        for i in mnIdx:
            print(i, end=' ')