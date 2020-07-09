from collections import deque

def solution(participant, completion):
    participant.sort()
    completion.sort()
    participant = deque(participant)
    completion = deque(completion)
    while completion:
        runner = participant.popleft()
        complete = completion.popleft()
        if runner != complete:
            answer = runner
            return answer
    answer = participant[0]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "mislav", "ana"]
print(solution(participant, completion))