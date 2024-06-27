import heapq

def solution(n, k, enemy):
    # 병사 n명 / 무족권 K번 사용 가능 / enemy 매 라운드 적의 수
    max_heap = []
    
    for round_num, e in enumerate(enemy):
        heapq.heappush(max_heap, -e)
        if n >= e:
            n -= e
        else:
            if k > 0:
                k -= 1
                n -= e
                # 무족권을 사용해도 병사가 부족한 경우, 가장 큰 적의 수를 복원
                if n < 0:
                    n += -heapq.heappop(max_heap)
            else:
                return round_num # 더 이상 방어 불가
            
    return len(enemy) # 모든 라운드 방어 가능