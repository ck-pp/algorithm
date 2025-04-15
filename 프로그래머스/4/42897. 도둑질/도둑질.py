# 인접한 두 집 털면 경보 울림

def solution(money):
    # 돈의 최댓값 & 전 집 선택o/x 중 max값 저장
    n = len(money)
    # dp 정의
    dp = [0 for _ in range(n)]
    
    # 첫번째 집 선택했을 경우
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[0] + money[2]
    
    # 마지막 집이 첫번째 집과 인접하므로 선택X
    for i in range(3, n-1):
        # 바로 이전값은 선택X
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]
    
    # 첫번째 집 선택했을때 최댓값 저장
    max1 = max(dp)
    
    # 첫번째 집 선택 안했을 경우
    # 첫번째 집이 최댓값일 수 있으므로(= dp[0]이 max) 0으로 저장
    dp[0] = 0
    dp[1] = money[1]
    dp[2] = money[2]
    
    for j in range(3, n):
        dp[j] = max(dp[j-2], dp[j-3]) + money[j]
    
    # 첫번째 집 선택 안했을때 최댓값 저장
    max2 = max(dp)
    
    return max(max1, max2)