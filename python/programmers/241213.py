# https://school.programmers.co.kr/learn/courses/30/lessons/42842 
# 카펫
def solution(brown, yellow):
    brown = (brown - 4)//2
    
    for i in range(1, brown):
        if (brown-i)*i == yellow:
            return [brown-i+2, i+2]