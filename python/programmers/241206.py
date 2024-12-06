# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    w_size = 0
    h_size = 0
    for size in sizes :
        size.sort()
        w_size = max(w_size, size[0])
        h_size = max(h_size, size[1])
        
    return w_size * h_size