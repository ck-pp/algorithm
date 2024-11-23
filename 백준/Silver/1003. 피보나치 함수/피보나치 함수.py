import sys

input = sys.stdin.readline
T = int(input())

# [0의 개수, 1의 개수]
dp = [[0, 0] for _ in range(41)]  # N의 최대 범위가 40이므로
dp[0] = [1, 0]
dp[1] = [0, 1]

# 2 ~ 41 dp 배열 값 채우기
for n in range(2, 41):
    dp[n][0] = dp[n-1][0] + dp[n-2][0]
    dp[n][1] = dp[n-1][1] + dp[n-2][1]

for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])