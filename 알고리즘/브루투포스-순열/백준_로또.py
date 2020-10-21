from itertools import combinations

flag = True

while flag:
    S = list(map(int, input().split()))
    n = S[0]
    if not n:
        flag = False
        break
    S.remove(S[0])

    for case in combinations(S, 6):
        print(' '.join(map(str, case)))
    print('')


