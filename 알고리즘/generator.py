def prime_number_list(number):
    def prime_number(number):
        if number != 1:
            for f in range(2, number):
                if number % f == 0:
                    return False
        else:
            return False
        return True

    integer_list = (x for x in range(2, number + 1))
    prime_numbers = []
    for num in integer_list:
        if prime_number(num):
            prime_numbers.append(num)

    return prime_numbers


def prime_number_dict(number, prime_numbers) -> dict:
    result = {}
    for prime in prime_numbers:
        degree = 0
        while number % prime == 0:
            degree += 1
            number = number // prime
        result[prime] = degree
        if number == 1:
            break
    return result


number = int(input())
result = [{1:1}]
for num in range(number, 1, -1):
    prime_numbers = prime_number_list(num)
    print_dict = prime_number_dict(num, prime_numbers)
    result.append(print_dict)

print(result)