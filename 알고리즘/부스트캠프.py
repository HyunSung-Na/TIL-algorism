def solution(name_list):
    answer = False
    for name in name_list:
        for index in range(len(name_list)):
            if name_list[index] == name:
                continue
            else:
                index1 = 0
                print(name_list[index])
                while len(name_list[index]) - index1 >= len(name):
                    if name_list[index][index1:index1 + len(name)] == name:
                        return True
                    else:
                        index1 += 1
    return answer

name_list = ["봄", "여름", "봄봄"]
name_list2 = ["너굴", "너울", "여울", "서울"]
name_list3 = ["가을", "우주", "너굴"]

print(solution(name_list3))