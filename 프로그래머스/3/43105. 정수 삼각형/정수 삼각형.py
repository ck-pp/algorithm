
def solution(triangle):
    # dp 정의
    # dp[i][j]: i번째 행 j번째 열까지 거쳐간 숫자(합)의 최댓값 
    dp = [row for row in triangle]
    
    # 행 길이
    n = len(triangle)
    
    for i in range(1, n):
        # 열 길이
        m = len(triangle[i])
        for j in range(len(triangle[i])):
            
            # 1. 각 행의 왼쪽 끝자리 수일 경우
            if j == 0:
                dp[i][j] += dp[i-1][j]
                
            # 2. 각 행의 오른쪽 끝자리 수일 경우
            elif j == m-1:
                dp[i][j] += dp[i-1][j-1]
                
            # 3. 각 행의 양 끝이 아닐 경우
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    
    return max(dp[n-1])