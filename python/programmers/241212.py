# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3 폰켓몬
def solution(nums):
    return min(len(nums)/2, len(set(nums)))