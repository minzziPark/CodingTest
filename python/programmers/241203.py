# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_book.sort()
    hash_map = {}
    
    for phone in phone_book :
        if len(hash_map) == 0 :
            hash_map[hash(phone)] = phone
        else :
            for i in range(1, len(phone)):
                if hash(phone[:i]) in hash_map:
                    return False
            hash_map[hash(phone)] = phone
                
    return True