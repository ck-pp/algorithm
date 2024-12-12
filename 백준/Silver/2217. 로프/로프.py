import sys
imput = sys.stdin.readline

N = int(input())
max_weights = list(int(input()) for _ in range(N))

# k개 로프 -> w 중량: 각각 w/k 중량
sorted_weights = sorted(max_weights, reverse=True)
# w/k이므로 최대 -> 가장 작은 중량을 들 수 있는 로프 * 전체 로프 개수
# 아니면 중량 작은 로프 빼고 계산한 값과 비교해서 더 큰 값으로!
res = []
for i in range(N):
    res.append(sorted_weights[-1] * (N - i))
    sorted_weights.pop()

print(max(res))