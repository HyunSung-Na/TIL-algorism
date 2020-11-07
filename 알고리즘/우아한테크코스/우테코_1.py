grade_score = {
    'A+': 10,
    'A0': 9,
    'B+': 8,
    'B0': 7,
    'C+': 6,
    'C0': 5,
    'D+': 4,
    'D0': 3,
    'F': 0
}


def score_result(grade):
    return grade_score[grade]


def weight_result(grade, weight):
    return grade * weight


def solution(grades, weights, threshold):
    result = []
    sum_score = 0
    for grade in grades:
        result.append(score_result(grade))
    for index in range(len(weights)):
        sum_score += weight_result(result[index], weights[index])
    answer = sum_score - threshold
    return answer


grades = ["A+", "D+", "F", "C0"]

weights = [2, 5, 10, 3]

threshold = 50

print(solution(grades, weights, threshold))
