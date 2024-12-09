# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if s[i] == ')': answer -= 1
        else : answer += 1
        if answer < 0 : return False
    
    if answer == 0 : return True
    else : return False