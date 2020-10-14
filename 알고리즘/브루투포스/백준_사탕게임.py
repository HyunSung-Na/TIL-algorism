n = int(input())

candy = []
max_candy = 0

for _ in range(n):
    input_list = input()
    temp = []
    for i in input_list:
        temp.append(i)
    candy.append(temp)

def check(candy):
    candy_len = len(candy)
    result = 1
    for i in range(candy_len):
        same = 1
        for j in range(1, candy_len):
            if candy[i][j] == candy[i][j - 1]:
                same += 1
            else:
                same = 1
            if result < same:
                result = same
        same = 1
        for j in range(1, candy_len):
            if candy[j][i] == candy[j-1][i]:
                same += 1
            else:
                same = 1
            if result < same:
                result = same
    return result

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            check_candy = check(candy)
            if check_candy > max_candy:
                max_candy = check_candy
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i + 1 < n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            check_candy = check(candy)
            if check_candy > max_candy:
                max_candy = check_candy
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(max_candy)