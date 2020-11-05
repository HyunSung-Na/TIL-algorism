N, L = list(map(int, input().split()))

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
x, y = 0, 0


def go(place, L):

    checked = [False] * N

    for i in range(1, N):
        if place[i - 1] != place[i]:
            diff = abs(place[i] - place[i - 1])
            if diff != 1:
                return False
            if place[i - 1] < place[i]:
                for j in range(1, L + 1):
                    if i - j < 0:
                        return False
                    if place[i - 1] != place[i - j]:
                        return False
                    if checked[i - j]:
                        return False
                    checked[i - j] = True

        else:
            for k in range(1, L):
                if i + k >= N:
                    return False
                if place[i] != place[i + k]:
                    return False
                if checked[i + k]:
                    return False
                checked[i + k] = True

    return True


for p in range(N):
    temp_place = [-1] * N
    for o in range(N):
        temp_place[p] = array[p][o]
    if go(temp_place, L):
        result += 1

for p in range(N):
    temp_place = [-1] * N
    for o in range(N):
        temp_place[p] = array[o][p]

    if go(temp_place, L):
        result += 1


print(result)