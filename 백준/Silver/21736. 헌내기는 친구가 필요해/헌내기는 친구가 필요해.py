import sys
from collections import deque
imput = sys.stdin.readline

def bfs(start):
    dpos = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 이동
    q = deque([start])
    visited = set([start])
    cnt = 0  # 만난 사람의 수

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in dpos:
            next_x, next_y = cur_x + dx, cur_y + dy

            # 캠퍼스 내에서 벽이 아니고 방문하지 않은 곳만 탐색한다.
            if 0 <= next_x < M and 0 <= next_y < N and infos[next_y][next_x] != 'X':
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))
                    if infos[next_y][next_x] == 'P':  # 사람을 만난 경우
                        cnt += 1
    
    return cnt
    
                        
N, M = map(int, input().split())
infos = [list(input().strip()) for _ in range(N)]
start = None  # 아무 타입이나 저장 가능하도록!

for i in range(N):
    for j in range(M):
        if infos[i][j] == 'I':  # 도연이 위치 저장
            start = (j, i)  # (x, y)
            
res = bfs(start)
print(res if res > 0 else 'TT')  # 아무도 만나지 못한 경우 TT를 출력한다.