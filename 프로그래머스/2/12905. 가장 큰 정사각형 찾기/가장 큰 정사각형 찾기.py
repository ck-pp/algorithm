def solution(board):
    ans = 0
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                if x == 0 or y == 0:
                    dp[x][y] = 1
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
                ans = max(ans, dp[x][y])

    return ans ** 2