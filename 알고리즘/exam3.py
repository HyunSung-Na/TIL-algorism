n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data: #입력받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count +=1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('No')
        exit(0)

print('\n'.join(result))

