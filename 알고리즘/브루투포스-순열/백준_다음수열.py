n = int(input())
search = list(map(int, input().split()))
nums = []

k = -1

for i in range(len(search) - 1):
    if search[i] < search[i + 1]:
        k = i

if k == -1:
    print(-1)
else:
    for j in range(k + 1, len(search)):
        if search[k] < search[j]:
            m = j

    search[k], search[m] = search[m], search[k]
    temp = search[k+1:]
    temp.sort()
    answer = search[:k+1] + temp

    for num in answer:
        print(num, end=' ')
    print()