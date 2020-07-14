from collections import Counter

def solution(participant, completion):
    return [runner for runner, num in Counter(participant + completion).items() if num % 2].pop()
