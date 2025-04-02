import sys
input = sys.stdin.readline

N = int(input())

dp = [[0, 1] for _ in range(N+1)]  # (i자리 0으로 끝나는 이진수 개수, i자리 1로 끝나는 이진수 개수)

# 1. dp 값 계산하기
for i in range(2, N+1):
    # 0으로 끝난 수 > 1로 끝나는 수 1개 + 0으로 끝나는 수 1개
    # 1로 끝난 수 > 0으로 끝나는 수 1개
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    
# 2. N자리 이친수의 개수 출력하기
print(dp[N][0] + dp[N][1])