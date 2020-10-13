import itertools

little = []
result = list()

for _ in range(9):
    little.append(int(input()))

combine = itertools.combinations(little, 7)

for i in combine:
    if sum(i) == 100:
        result = list(i)
        break

result.sort()
for i in result:
    print(i)