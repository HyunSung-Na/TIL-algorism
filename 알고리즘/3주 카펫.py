def solution(brown, red):
    for index in range(1, red + 1):
        if red % index == 0:
            length = red // index
            if (((index + 2) * (length + 2)) - (index * length)) == brown:
                return [max(index + 2, length + 2), min(index + 2, length + 2)]