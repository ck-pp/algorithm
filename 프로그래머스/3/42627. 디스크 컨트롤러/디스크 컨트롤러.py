import heapq as hq

def solution(jobs):
    ans = 0
    now = 0
    n = len(jobs)
    
    # 요청 시각 순 정렬
    jobs.sort(key=lambda x: x[0])
    
    # 작업 소요 시간 짧은(min) - 요청 시각 빠른(min) - 작업 번호 작은(min) 순
    # 최소 힙
    queue = []
    
    idx = 0
    # 처리할 작업이 남아있는 동안 Or 대키 큐에 작업이 남아있는 동안
    while idx < n or queue:
        # 1. 현재까지 요청 들어온 작업 대기 큐에 저장
        while idx < n and jobs[idx][0] <= now:
            s, l = jobs[idx]
            hq.heappush(queue, (l, s))
            idx += 1
        
        # 2. 대기 큐에서 우선순위 높은 작업 꺼내 실행
        if queue:
            l, s = hq.heappop(queue)
            # 현재 시각 업데이트
            now += l
            # 반환 시간 합 업데이트
            ans += (now - s)
            
        # 3. 아직 요청된 작업이 없으면 다음 작업 요청 시각으로 점프
        else:
            now = jobs[idx][0]
    
    return ans // n