from collections import deque
import math

def solution(players, m, k):
    ans = 0
    servers = deque()
    N = len(players)
    
    for i in range(N):
        # 필요한 서버 수
        n = players[i] // m
        # 현재 운영 중인 서버 수
        current = len(servers)
        
        # 부족하면 그만큼 서버 추가
        if m <= players[i] and current < n:
            add_count = n - current
            servers.extend([k] * (add_count))
            ans += add_count
            
        # 이번 시간대가 끝난 후 모든 서버 시간 1씩 차감
        for j in range(len(servers)):
            servers[j] -= 1

        # 만료된 서버는 왼쪽에서부터 제거
        while servers and servers[0] < 1:
            servers.popleft()
    
    return ans