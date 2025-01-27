import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
# 오름차순 정렬
weights.sort()

# 측정 가능한 범위 최소값 초기화
target = 1
for weight in weights:
    # 측정 가능한 범위를 초과한 추라면 종료
    if weight > target:
        break
    
    target += weight
    
print(target)