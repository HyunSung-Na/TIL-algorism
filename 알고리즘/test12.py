def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    distance_left = [3,0]
    distance_right = [3,2]
    point = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for i in numbers:
        if i in left:
            distance_left = point[i]
            answer += "L"
        elif i in right:
            distance_right = point[i]
            answer +="R"
        else:
            left_point =abs(distance_left[0]-point[i][0])+abs(distance_left[1]-point[i][1])
            right_point = abs(distance_right[0]-point[i][0])+abs(distance_right[1]-point[i][1])
            if left_point < right_point:
                distance_left = point[i]
                answer += "L"
            elif right_point < left_point:
                distance_right = point[i]
                answer += "R"
            else:
                if hand == "left":
                    distance_left = point[i]
                    answer += "L"
                else:
                    distance_right = point[i]
                    answer += "R"
    return answer