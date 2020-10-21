n = int(input())

DAY = 0
PAY = 1
result = -999999999
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

def solution(day, total):
    global result
    if day == n:
        result = max(result, total)
        return
    if day > n:
        return
    solution(day + 1, total)
    solution(day + array[day][DAY], total + array[day][PAY])

solution(0, 0)
print(result)
