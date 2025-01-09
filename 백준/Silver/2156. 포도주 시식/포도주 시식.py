import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]  # 인덱스 1부터 시작

dp = [0] * (n + 1)  # dp[i]: i번째 잔까지 고려했을때, 최대로 마실 수 있는 포도주 양

# 초기값 설정
dp[1] = wines[1]
if n > 1:
    dp[2] = wines[1] + wines[2]

for i in range(3, n+1):
    # 1. 현재(= i번째) 포도주 마시지 않을 경우
    # 2. 현재 포도주 마시고, 바로 이전 포도주 마시지 않을 경우
    # 3. 현재 포도주와 바로 이전 포도주 마시고, 두번째 전 잔 마시지 않는 경우
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])
    
print(dp[n])  # 또는 dp[-1]