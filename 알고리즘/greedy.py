coin_list = [500,100,50,1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num*coin
        details.append([coin, coin_num])
    return print([total_coin_count, details])

min_coin_count(4720, coin_list)

def get_max_value(data_list1,capacity):
    data_list1 = sorted(data_list1, key = lambda x: x[1] / x[0],reverse= True)
    total_value = 0
    details = list()

    for data in data_list1:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0],data[1],1])
        else:
            fraction = capacity/data[0]
            total_value += data[1] * fraction
            details.append([data[0],data[1],fraction])
            break
    return print([total_value,details])
data_list1 = [(10,10),(15,12),(20,10),(25,8),(30,5)]
get_max_value(data_list1,30)
