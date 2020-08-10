N = 14
count = 0
a = 1
while N > 0:
    if N < a:
        a = 1
    else:
        N -= a
        count += 1
        a += 1

print(count)