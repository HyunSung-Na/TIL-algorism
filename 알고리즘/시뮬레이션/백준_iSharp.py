sharp = list(map(str, input().split()))

for i in range(1, len(sharp)):
    validation = list(sharp[i])
    end = []
    alpha = []
    for j in range(len(validation) - 1):
        if not validation[j].isalpha():
            end.append(validation[j])
        else:
            alpha.append(validation[j])
    end = end[::-1]
    result = []
    for k in range(len(end)):
        if end[k] == '[':
            result.append(']')
        elif end[k] == ']':
            result.append('[')
        else:
            result.append(end[k])

    word = sharp[0] + ''.join(result)
    print(word + " " + ''.join(alpha) + ";")
