import sys
input = sys.stdin.readline

n = int(input())
triangles = [list(map(int, input().split())) for _ in range(n)]

dp = [row for row in triangles]
for i in range(1, len(dp)):
    for j in range(len(dp[i])):
        if j == 0:  # 맨 왼쪽
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i]) - 1:  # 맨 오른쪽
            dp[i][j] += dp[i-1][j-1]
        else:  # 그 사이
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))