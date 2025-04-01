import sys
input = sys.stdin.readline

# 1. 피보나치 수 초기화(0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1)
dp = [0 for _ in range(46)]
dp[1] = 1

n = int(input())

# 2. 피보나치 수 구하기
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

# 3. n번째 피보나치 수 출력
print(dp[n])