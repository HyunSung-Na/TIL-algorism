def clap(num):
    num_list = list(str(num))
    clap_num = ['3', '6', '9']
    count = 0
    for num_one in num_list:
        if num_one in clap_num:
            count += 1
    return count


def solution(number):
    answer = 0
    for num in range(1, number + 1):
        answer += clap(num)
    return answer

number = 13

print(solution(number))



