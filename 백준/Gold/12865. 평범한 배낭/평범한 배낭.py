import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weights_values = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(K+1)]  # dp[j]: 무게 j 이하로 담을 수 있는 최대 가치

for w, v in weights_values:
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력
print(max(dp))