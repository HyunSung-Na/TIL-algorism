def do_sort(students):
    grade = sorted(students, key= lambda x: x[1], reverse=True)
    for index in range(len(grade)):
        if grade[index][1] == grade[index-1][1]:
            grade[index-1], grade[index] = grade[index], grade[index-1]
    return grade

def print_outputs(students):
    for student in students:
        if student[2] == 'a':
            print('Good A: {}'.format(student[0]))
        if student[2] == 'b':
            print('Great B: {}'.format(student[0]))
        if student[2] == 'c':
            print('Best C: {}'.format(student[0]))


students = [['Paul', 90, 'a'], ['Michael', 50, 'b'], ['Gina', 90, 'c'], ['Marie', 70, 'b']]

sorted_students = do_sort(students)
print_outputs(sorted_students)


from itertools import combinations

a = [-25, -10, -7, -3, 2, 4, 8, 10]

def solution(a):
    sum_zero = []
    list_number = combinations(a, 3)
    for number in list_number:
        if not sum(number):
            sum_zero.append(list(number))
    return print(sum_zero)

solution(a)