def solution(votes, k):
    cars = dict()
    car_list = []
    for i in votes:
        cars.update({i: votes.count(i)})
    for key, v in cars.items():
        car_list.append([key, v])
    car_list = sorted(car_list, key=lambda x: x[1], reverse=True)
    sum_rank = 0
    for i in range(k):
        sum_rank += car_list[i][1]
    while sum_rank > 0 and len(car_list) > 0:
        last_car = car_list.pop()
        sum_rank -= last_car[1]
    if len(car_list):
        answer = car_list[-1][0]
    else:
        answer = votes[-1]
    return answer


votes = ["AAD", "AAA", "AAC", "AAB"]
k = 4

print(solution(votes, k))