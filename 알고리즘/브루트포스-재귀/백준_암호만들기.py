m, n = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()


def check(password):
    ja = 0
    mo = 0
    mo_list = ['a', 'e', 'i', 'o', 'u']
    for pwd in password:
        if pwd in mo_list:
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def solution(m, alpha, password, index):
    if len(password) == m:
        if check(password):
            print(password, end='\n')
        return

    if len(alpha) <= index:
        return

    solution(m, alpha, password + alpha[index], index+1)
    solution(m, alpha, password, index+1)

solution(m, alpha, '', 0)