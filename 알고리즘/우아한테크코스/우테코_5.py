def duplication_check(data, penter, pexit, perscape):
    slice_len = len(penter)
    slice_count = len(data) // slice_len
    result = []
    for index in range(slice_count):
        first = index * slice_len
        end = (index + 1) * slice_len
        slice_data = data[first:end]
        if penter == slice_data:
            slice_data = perscape + slice_data
        elif pexit == slice_data:
            slice_data = perscape + slice_data
        elif perscape == slice_data:
            slice_data = perscape + slice_data
        result.append(slice_data)
    return result


def solution(penter, pexit, pescape, data):
    result = duplication_check(data, penter, pexit, pescape)
    answer = penter + ''.join(result) + pexit
    return answer

penter = "10"
pexit = "11"
pescape = "00"
data = "00011011"
"100000010010001111"
print(solution(penter, pexit, pescape, data))