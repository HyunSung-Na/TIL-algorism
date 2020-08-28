def Prime(n):
    prime_num = []
    for num in range(1, n+1):
        if not n % num:
            prime_num.append(num)
    return prime_num

def Prime2(n, m):
    prime_num = []
    for num in range(1, m + 1):
        prime_num.append(num * n)
    return prime_num

def solution(n, m):
    answer = []
    n_prime = set(Prime(n))
    m_prime = set(Prime(m))
    if not len(n_prime) or not len(m_prime):
        min_prime = 1
    else:
        min_prime = max(n_prime & m_prime)
    answer.append(min_prime)
    n_prime2 = set(Prime2(n, m))
    m_prime2 = set(Prime2(m, n))
    if not len(n_prime2) or not len(m_prime2):
        answer.append(0)
        return answer
    max_prime = min(n_prime2 & m_prime2)
    answer.append(max_prime)
    return answer


n = 3
m = 12

print(solution(n, m))