# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    curr_idx = location
    max_num = max(priorities)
    answer = 0
    
    while True :
        process = priorities[0]
        priorities.pop(0)
        
        if process < max_num :
            priorities.append(process)
        else :
            answer += 1
            if curr_idx == 0 :
                break
            else :
                max_num = max(priorities)
            
        curr_idx -= 1
        if curr_idx < 0 :
            curr_idx = len(priorities) - 1
        
    return answer