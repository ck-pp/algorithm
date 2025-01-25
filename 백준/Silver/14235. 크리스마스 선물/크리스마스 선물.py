import sys
import heapq
input = sys.stdin.readline

n = int(input())
bundle = []  # 선물 보따리(최대-힙)

for _ in range(n):
    a = list(map(int, input().split()))
    
    if a[0] > 0:  # 거점지인 경우
        for i in range(1, len(a)):  # 선물 추가
            heapq.heappush(bundle, -a[i])
    else:  # 거점지가 아닌 경우
        if bundle:
            # 선물 가치 출력
            print(-heapq.heappop(bundle))
        else:
            print(-1)