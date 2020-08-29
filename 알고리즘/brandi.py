from threading import Timer
import time

user_input = int(input())

def max_heart(user_input):
    return 220 - user_input

def heart_rate(heart, max):
    return float(heart) / float(max)

one_point = 60
one_count = 0
two_point = 68
two_count = 0
three_point = 75
three_count = 0
four_point = 80
four_count = 0
five_point = 90
five_count = 0
six_point = 90
six_count = 0
lines = []
while True:
    first_time = time.time()
    timeout = 1
    t = Timer(timeout, print, [''])
    t.start()
    line = input()
    if not line:
        break
    lines.append(line)
    t.cancel()
    last_time = time.time() - first_time
    if last_time > 2:
        break
max_user = max_heart(user_input)
for heart in lines:
    rate = heart_rate(int(heart), max_user) * 100
    if rate < one_point:
        one_count += 1
    elif rate < two_point:
        two_count += 1
    elif rate < three_point:
        three_count += 1
    elif rate < four_point:
        four_count += 1
    elif rate < five_point:
        five_count += 1
    elif rate >= six_point:
        six_count += 1
print("{} {} {} {} {} {}".format(six_count, five_count, four_count, three_count, two_count, one_count))