NOTATION = '0123456789ABCDEF'

def numChange(num, base):
    q, r = divmod(num, base)
    n = NOTATION[r]
    return numChange(q, base) + n if q else n

def solution(n):
    answer = 0
    three = numChange(n, 3)
    print(three)
    ten = three[::-1]
    answer = int(ten, 3)
    return answer

n = 45
print(solution(n))