import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    
    dp = [0] * (11)
    dp[1], dp[2], dp[3] = 1, 2, 4
    
    for i in range(4, n + 1):
        # 1, 2, 3의 합으로 나타내기 때문에 아래와 같은 점화식을 가진다.
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])