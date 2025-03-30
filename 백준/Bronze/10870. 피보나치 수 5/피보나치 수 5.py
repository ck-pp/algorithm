import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(21)]

dp[1] = 1  # dp[0] = 0, dp[1] = 1

# 피보나치 수열 값 채우기(dp)
for i in range(2, 21):
    dp[i] = dp[i-1] + dp[i-2]

# n번째 피보나치 수 출력
print(dp[N])