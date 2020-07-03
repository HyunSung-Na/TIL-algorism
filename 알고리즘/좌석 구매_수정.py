def solution(seat):
    answer = len(set(map(tuple,seat)))
    return answer