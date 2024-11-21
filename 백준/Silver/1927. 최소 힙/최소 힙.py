import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
heapq.heapify(arr)

for _ in range(N):
    num = int(input())
    
    if num > 0:
        heapq.heappush(arr, num)
    else:
        if len(arr) > 0: print(heapq.heappop(arr))
        else: print(0)