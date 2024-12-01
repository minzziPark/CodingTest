# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    hash_map = {}
    
    for (cloth, category) in clothes:
        if category in hash_map:
            hash_map[category].append(cloth)
        else :
            hash_map[category] = [cloth]
    
    for hash_key in hash_map.keys():
        answer *= (len(hash_map[hash_key])+1)
    
    return answer-1