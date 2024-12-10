# https://school.programmers.co.kr/learn/courses/30/lessons/42626 더 맵게
import heapq

def solution(scoville, K):
    count = 0
    heap = scoville
    heapq.heapify(heap)
    
    while heap[0] < K and len(heap) > 1 :
        mix = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        if len(heap) == 0 and mix < K :
            return -1
        heapq.heappush(heap, mix)
        count += 1

    return count