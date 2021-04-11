n, m = list(map(int, input().split()))
array = []

for i in range(1001):
    for j in range(i, 0, -1):
        array.append(i)

print(sum(array[n-1:m]))

