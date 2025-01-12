import sys
input = sys.stdin.readline

n = int(input())

# 2원, 5원
# dp[i]: 금액 i 만들기 위해 필요한 최소 동전 개수
dp = [float('inf')] * (n + 1)
dp[0] = 0

# 점화식
for i in range(2, n + 1):
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 1)  # 금액 i−2를 만들 수 있는 최소 동전에 2원을 추가
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)  # # 금액 i−5를 만들 수 있는 최소 동전에 5원을 추가
        
print(dp[n] if dp[n] != float('inf') else -1)