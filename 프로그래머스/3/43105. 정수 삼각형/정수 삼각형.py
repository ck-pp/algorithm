def solution(triangle):
    dp = [[0] * len(row) for row in triangle]
    
    for h in range(len(triangle)):
        for n in range(h + 1):
            if n == 0: # 왼쪽 끝
                dp[h][n] = dp[h-1][n] + triangle[h][n]
            elif n == h: # 오른쪽 끝
                dp[h][n] = dp[h-1][n-1] + triangle[h][n]
            else:
                dp[h][n] = max(dp[h-1][n-1], dp[h-1][n]) + triangle[h][n]

    return max(dp[-1])