from collections import deque

# 칸의 개수 최솟값 & 가중치 없음 -> bfs
def solution(maps):
    n = len(maps[0])  # 행 길이
    m = len(maps)  # 열 길이
    
    q = deque([((0, 0), 1)])  # (현재 위치 좌표, 지나온 칸의 개수)
    visited = set([(0, 0)])
    
    dpositions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 동, 서, 남, 북 이동 가능
    
    # bfs 로직 실행
    while q:
        cur_pos, steps = q.popleft()
        
        # 상대 팀 진영에 도착한 경우
        if cur_pos == (n-1, m-1):
            return steps
        
        for x, y in dpositions:
            n_x, n_y = cur_pos[0] + x, cur_pos[1] + y
            
            # 문제에서 주어진 조건
            # 1) 게임 맵 벗어난 길 갈 수 없음 2) 벽이 아닌 길
            if 0 <= n_x < n and 0 <= n_y < m and maps[n_y][n_x] == 1:
                if (n_x, n_y) not in visited:
                    q.append(((n_x, n_y), steps + 1))
                    visited.add((n_x, n_y))
                    
    return -1
        
        
        