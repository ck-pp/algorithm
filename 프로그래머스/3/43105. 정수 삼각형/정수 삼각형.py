def solution(triangle):
    ans = 0
    dp = [[triangle[0][0]] * n for n in range(1, len(triangle)+1)]
    for h in range(1, len(triangle)):
        for num in range(h+1):
            if num == 0:
                dp[h][num] = dp[h-1][num] + triangle[h][num]
            elif num == h:
                dp[h][num] = dp[h-1][num-1] + triangle[h][num]
            else:
                dp[h][num] = max(dp[h-1][num-1], dp[h-1][num]) + triangle[h][num]
    return max(dp[-1])