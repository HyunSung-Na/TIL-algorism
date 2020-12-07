def solution(page, broken):
    enable = {str(i) for i in range(10)}
    enable -= set(map(str, broken))
    min_cnt = abs(100 - page)

    for num in range(1000001):
        num = str(num)
        for j in range(len(num)):
            if num[j] not in enable:
                break
            elif j == len(num) - 1:
                min_cnt = min(min_cnt, abs(page - int(num)) + len(str(num)))
    return min_cnt
page = 99999
broken = [0,2,3,4,5,6,7,8,9]
print(solution(page, broken))

