def solution(m, n, puddles):
    # 최단경로x, 최단경로 개수 = dp 사용
    # (1, 1) (m, n) -> (0, 0) (m-1, n-1)
    # dp 정의
    # dp[i][j]: (j, i) 좌표까지의 최단경로 개수
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    # 물 웅덩이 -1로 표시
    for x, y in puddles:
        dp[y-1][x-1] = -1
    
    # 오른쪽, 아래쪽으로만 이동
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                if 0 < i: dp[i][j] += dp[i-1][j]
                if 0 < j: dp[i][j] += dp[i][j-1]
                
    return dp[n-1][m-1] % 1000000007