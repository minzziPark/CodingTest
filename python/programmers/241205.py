# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for (i, j, k) in commands :
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer