import itertools

def solution(numbers):
    number_combine = itertools.permutations(numbers, 3)
    result = []
    for num1, num2, num3 in number_combine:
        result.append(int(str(num1) + str(num2) + str(num3)))
    return str(sorted(result, reverse=True)[0])

numbers = [6, 10, 2]

print(solution(numbers))


def solution1(intervals):
    if not intervals:
        return []
    data = []
    for interval in intervals:
        data.append((interval[0], 0))
        data.append((interval[1], 1))
    data.sort()

    merged = []
    stack = [data[0]]
    for i in range(1, len(data)):
        d = data[i]
        if d[1] == 0:
            # this is a lower bound, push this onto the stack
            stack.append(d)
        elif d[1] == 1:
            if stack:
                start = stack.pop()
            if len(stack) == 0:
                # we have found our merged interval
                merged.append((start[0], d[0]))
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(solution1(intervals))


def solution2(s1, s2, s3):
    combine = s1 + s2
    combine_list = sorted(list(combine))
    result_list = sorted(list(s3))
    combine_char = ''.join(combine_list)
    result_char = ''.join(result_list)
    if combine_char == result_char:
        return True
    return False


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print(solution2(s1, s2, s3))