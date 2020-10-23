from itertools import combinations

n = int(input())

array = [list(map(int, input().split())) for x in range(n)]

team = [i for i in range(n)]

result = 999999999

combine_team = list(combinations(team, n // 2))

for team1 in combine_team:
    team2 = [x for x in team if x not in team1]
    first_sum = 0
    second_sum = 0
    for x, y in list(combinations(team1, 2)):
        first_sum += array[x][y] + array[y][x]
    for x, y in list(combinations(team2, 2)):
        second_sum += array[x][y] + array[y][x]

    result = min(result, abs(first_sum - second_sum))

print(result)

