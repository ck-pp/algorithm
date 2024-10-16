import copy as c

def solution(triangle):
    dp = c.deepcopy(triangle)
    # 왼쪽 대각선 아래: [row+1][col], 오른쪽 대각선 아래: [row+1][col+1]
    for row in range(1, len(dp)):
        for col in range(len(dp[row])):
            if col == 0:  # 맨 왼쪽
                dp[row][col] += dp[row-1][col]
            elif col == len(dp[row]) - 1:  # 맨 오른쪽
                dp[row][col] += dp[row-1][col-1]
            else:  # 그 사이
                dp[row][col] += max(dp[row-1][col-1], dp[row-1][col])
    
    return max(dp[-1])