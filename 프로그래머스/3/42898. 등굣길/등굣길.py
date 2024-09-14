def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1
        
    # 오른쪽, 아래쪽으로만 이동 가능
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] < 0:  # 물웅덩이
                dp[i][j] = 0
            else:
                if i > 1:
                    dp[i][j] += dp[i-1][j]
                if j > 1:
                    dp[i][j] += dp[i][j-1]
                    
    return dp[n][m] % 1000000007