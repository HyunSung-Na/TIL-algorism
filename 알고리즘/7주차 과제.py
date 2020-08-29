matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

def searchMatrix(data, target):
    matrix = []
    for num_list in data:
        matrix.extend(num_list)
    matrix.sort()
    start = 0
    end = len(matrix) - 1

    while start <= end:
        mid = (start + end) // 2

        if matrix[mid] == target:
            return True
        elif matrix[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

print(searchMatrix(matrix, 11))

