from collections import Counter

def solution(board):
    sum = 0
    n = len(board)
    dp = [[0 for _ in board] for _ in board]
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                dp[i][j] = 1
                for dx, dy in directions:
                    next_x, next_y = i+dx, j+dy
                    if (-1 < next_x < n and -1 < next_y < n) and not dp[next_x][next_y]:
                        dp[next_x][next_y] = 1
    for r in range(n):
        sum += Counter(dp[r])[0]
        
    return sum