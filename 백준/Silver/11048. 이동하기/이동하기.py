import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(N)]

dp = candies.copy()
# (1, 1) -> (N, M)을 (0, 0) -> (N-1, M-1)
# (r+1, c), (r, c+1), (r+1, c+1) 이동 가능
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:  # 출발점
            continue
        if i == 0:  # 첫번째 행
            dp[i][j] += dp[i][j-1]
        elif j == 0:  # 첫번째 열
            dp[i][j] += dp[i-1][j]
        else:  
            dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N-1][M-1])