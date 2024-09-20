# 인접한 두 집 털면 경보 울림

def solution(money):
    n = len(money)
    dp = [0 for _ in range(len(money))]
    
    # 첫 번째 집을 털었을 경우
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[2] + money[0]
    
    for i in range(3, n):
        # i-2, i-3 번쨰 값 중 큰 값 + 자신
        dp[i] = max(dp[i - 2], dp[i - 3]) + money[i]
    
    max1 = max(dp[:-1])  # 마지막 집 털지 못함(인접한 관계이므로)
    
    # 첫 번째 집을 털지 않았을 경우
    dp[0] = 0  # 첫 번째 집 money가 최댓값일 경우도 있기 때문에? 아예 값을 배제.
    dp[1] = money[1]
    dp[2] = money[2]
    
    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 3]) + money[i]
    
    max2 = max(dp)  # 마지막 집 털 수 있음

    return max(max1, max2)