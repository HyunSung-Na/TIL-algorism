result = []
    count = 0
    for i in range(len(strs)-1):
        if strs[0][0] != strs[i][0]:
            answer = '""'
            return answer
        else:
            for j in range(len(strs[i]-1)):
            while strs[0][j] == strs[i][j]:
                count += 1
                result.append(count)
            answer = strs[0][:min(result)]
a = ["abcaefg","abcdefg","abcdhfg"]
print(solution(a))