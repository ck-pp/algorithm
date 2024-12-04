import sys
from collections import deque
input = sys.stdin.readline

# 원형 큐 비슷한 문제 = 덱
N = int(input())
balloons = list(map(int, input().split()))
idx_balloons = deque([(idx + 1, value) for idx, value in enumerate(balloons)])

# 3 2 1 -3 -1 -> 1 4 5 3 2
bomb = 1
res = []
while idx_balloons:
    idx, bomb = idx_balloons.popleft()  # 현재 풍선 터뜨리기
    res.append(str(idx))
    
    if bomb > 0:
        idx_balloons.rotate(-(bomb-1))  # 현재 위치에서 한 칸 이동했으므로 -1 조정
    else:
        idx_balloons.rotate(-bomb)  # 음수 방향 이동

print(' '.join(res))