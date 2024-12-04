# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx, i in enumerate(completion) :
        if participant[idx] != i :
            return participant[idx]
    return participant[-1]