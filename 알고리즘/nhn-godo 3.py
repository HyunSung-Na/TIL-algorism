import collections


def solution(s, n):
    count = collections.Counter(s)
    s = list(s)
    max_count = max(count.values())
    min_count = min(count.values())
    result_max = []
    result_min = []
    for alpha, num in count.items():
        if max_count == num:
            result_max.append(alpha)
        if min_count == num:
            result_min.append(alpha)

    if min_count <= n:
        n -= min_count
        count.popitem()
        s.remove(result_min.pop())
        count = collections.Counter(s)
        min_count = min(count.values())
    else:
        if max_count >= n:
            for i in range(n):
                max_alpha = result_max[0]
                if max_alpha in s:
                    s.remove(max_alpha)
        else:
            while result_max[0] in s:
                s.remove(result_max[0])
                n -= 1
    count = collections.Counter(s)
    max_count = max(count.values())
    if min_count >= max_count:
        return 0
    if min_count + max_count > n:
        ans = (max_count - min_count) - n
    else:
        ans = 0
    return ans

s = "aaaabbbbc"
n = 0

print(solution(s, n))