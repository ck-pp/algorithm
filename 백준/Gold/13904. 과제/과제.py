import sys
import heapq
input = sys.stdin.readline

# 마감일 내에서 과제를 처리할 수 있는 날은 제한되어 있으므로, 점수가 높은 과제를 우선적으로 선택해야 한다.
N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

# 과제 마감일까지 남은 일수 작은 순, 과제 점수 큰 순
tasks.sort(key=lambda x: (x[0], -x[1]))
pq = []  # 우선순위 큐

for d, w in tasks:
    heapq.heappush(pq, (w))
    
    if len(pq) > d:  # 마감일 초과하면 점수가 가장 낮은 과제 제거
        heapq.heappop(pq)
    
print(sum(pq))  # 남아있는 점수 합계 출력