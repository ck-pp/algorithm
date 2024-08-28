def solution(m, n, puddles):
    # dp[i][j]: 위치 (i, j)까지 도달할 수 있는 경로의 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점
    
    for puddle_x, puddle_y in puddles:
        dp[puddle_y][puddle_x] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0  # 물 웅덩이는 지나갈 수 없으므로
            else:
                if i > 1:
                    dp[i][j] += dp[i-1][j]  # 아래쪽 이동
                if j > 1:
                    dp[i][j] += dp[i][j-1]  # 오른쪽 이동
                dp[i][j] %= 1000000007
        
    return dp[n][m]