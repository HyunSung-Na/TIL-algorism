def solution(s):
    answer = []
    num = list(s)
    nums = 0
    change = 0

    while num:
        temp = []
        if num == '1':
            break
        for i in num:
            if i == '0':
                nums += 1
            else:
                temp.append(int(i))
        num = format(len(temp), 'b')
        change += 1
    answer.extend([change, nums])
    return answer

s = "110010101001"

print(solution(s))