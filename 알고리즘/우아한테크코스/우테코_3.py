def game(batting_money, expect, actual):
    if expect == actual:
        return batting_money
    else:
        return 0


def batting(money, count):
    return money * count


def all_in(money, batting_money):
    return batting_money > money


def solution(money, expected, actual):
    batting_count = 1
    batting_money = 100
    game_count = len(expected)
    for index in range(game_count):
        batting_money = batting(batting_money, batting_count)
        if all_in(money, batting_money):
            batting_money = money
            money = 0
        else:
            money -= batting_money
        game_result = game(batting_money, expected[index], actual[index])
        if game_result:
            money += batting_money
            batting_count = 1
            batting_money = 100
        else:
            batting_count = 2
        money += game_result
        if not money:
            break

    answer = money
    return answer

money = 1000
expected = ['H', 'T', 'H', 'T', 'H', 'T', 'H']
actual = ['T', 'T', 'H', 'H', 'T', 'T', 'H']

print(solution(money, expected, actual))