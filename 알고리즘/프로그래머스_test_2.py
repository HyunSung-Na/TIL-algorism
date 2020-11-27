import re

def solution(p,n):
    answer = ""
    time = re.sub('[:]', '', p)
    time1, time2 = time.split()
    time_hour = int(''.join(list(time2)[:2]))
    time_min = int(''.join(list(time2)[2:4]))
    time_sec = int(''.join(list(time2)[4:6]))

    if n < 60:
        time_sec += n
        while time_sec >= 60:
            time_sec -= 60
            time_min += 1
    if time_min >= 60:
        while time_min >= 60:
            time_min -= 60
            time_hour += 1
    if time1 == "PM":
        time_hour = int(''.join(time_hour)) + 12
    if time_hour >= 24:
        time_hour -= 24
    str_hour = str(time_hour)
    str_min = str(time_min)
    str_sec = str(time_sec)
    if len(str_min) < 2:
        str_min = "0" + str_min
    elif len(str_sec) < 2:
        str_sec = "0" + str_sec
    elif len(str_hour) < 2:
        str_hour = "0" + str_hour
    answer = str_hour + ":" + str_min + ":" + str_sec
    return answer

P = "PM 11:59:59"
N = 1

print(solution(P, N))
