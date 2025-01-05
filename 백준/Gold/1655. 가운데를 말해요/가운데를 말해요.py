import sys
import heapq
input = sys.stdin.readline

N = int(input())
left = []  # 최대 힙(중간값 이하)
right = []  # 최소 힙(중간값 이상)
for _ in range(N):
    num = int(input())
    
    # 1. 힙에 값 삽입
    if not left or num <= -left[0]:  # 최대 힙 -> 음수 저장
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
        
    # 2. 힙 크기 조정
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    
    # 3. 중간값 출력
    print(-left[0])  # 최대 힙의 루트값 = 중간값