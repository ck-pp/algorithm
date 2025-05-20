import heapq as hq

def solution(scoville, K):
    ans = 0    
    # 기본 min-heap
    hq.heapify(scoville)
    
    # 가장 작은 스코빌 지수가 K보다 작을 동안 반복
    # = 모든 스코빌 지수가 K 이상이 아닐 동안 반복
    while scoville[0] < K:
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) < 2:
            return -1
        
        new = hq.heappop(scoville) + hq.heappop(scoville) * 2
        hq.heappush(scoville, new)
        ans += 1
        
    return ans