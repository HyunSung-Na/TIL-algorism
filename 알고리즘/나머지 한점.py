import collections

def solution(v):
    answer = []
    for angle in zip(*v):
        y = collections.Counter(angle)
        answer.extend([angle for angle in y if y[angle] == 1])

    return answer

v = [[1, 1], [2, 2], [1, 2]]

print(solution(v))