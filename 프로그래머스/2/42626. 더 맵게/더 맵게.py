import heapq as hq

def solution(scoville, K):
    # 모든 음식 지수 K 이상될 때 까지
    # 가장 안 매운 음식 지수 + 2번째 안 매운 음식 지수 * 2
    
    hq.heapify(scoville)  # 최소 힙(min-heap)
    steps = 0  # 섞어야 하는 최소 횟수
    
    while scoville[0] < K:
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) < 2:
            return -1
        
        # 섞은 음식의 스코빌 지수
        new_scoville = hq.heappop(scoville) + hq.heappop(scoville) * 2
        hq.heappush(scoville, new_scoville)
        
        steps += 1
        
    return steps