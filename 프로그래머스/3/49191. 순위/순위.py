def solution(n, results):
    # 각 선수간의 승패 기록
    win = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 직접적 승패 관계 기록
    for A, B in results:
        win[A][B] = True
        
    # 플로이드-워셜 알고리즘 (간접적 승패 관계 기록)
    for k in range(1, n + 1):  # 중간 노드
        for i in range(1, n + 1):  # 출발 노드
            for j in range(1, n + 1):  # 도착 노드
                # i번이 k번을 이기고, k번이 j번을 이겼을 경우 i번이 j번을 이긴다.
                if win[i][k] and win[k][j]:
                    win[i][j] = True
                
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            # 자기 자신을 제외한 모든 선수(= n-1)와의 관계가 확실해야 함
            if win[i][j] or win[j][i]:
                cnt += 1
        if cnt == n - 1:
            ans += 1
    
    return ans