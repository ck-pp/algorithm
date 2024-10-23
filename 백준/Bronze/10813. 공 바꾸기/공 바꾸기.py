import sys

N, M = map(int,sys.stdin.readline().split())
basket_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
baskets = [num for num in range(1, N+1)]

for i, j in basket_infos:
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
    
for num in baskets:
    print(num)