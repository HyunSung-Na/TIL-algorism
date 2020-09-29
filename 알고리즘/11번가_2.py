def solution(S):
    answer = []
    index1 = 0
    index2 = []
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] == S[i - 1][j]:
                index1 = j
                if i - 1 < 0:
                    index2.append([i, len(S) - 1])
                    print(index2)
                else:
                    index2.append([i, i - 1])
    if index2:
        answer.extend(index2[0])
    else:
        return []
    answer.append(index1)
    return answer

S = ["abc", "bca", "dbe"]
S1 = ["bdafg", "ceagi"]
print(solution(S1))