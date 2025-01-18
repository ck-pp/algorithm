import sys
input = sys.stdin.readline

D, K = map(int, input().split())

for i in range(1, K // 2):
    # dp 배열 초기화(거꾸로)
    dp = [0] * (D + 1)
    dp[D] = K
    dp[D-1] = dp[D] - i
    for j in range(D - 2, 0, -1):
        temp_v = dp[j+2] - dp[j+1]
        if temp_v > dp[j+1]:  # dp[j]가 dp[j+1]보다 큰 경우 다시 dp 값 채우기
            break
        
        dp[j] = temp_v
        
    if dp[1] > 0:  # dp[1]이 처음 양수가 되는 경우를 저장
        break

print(dp[1])
print(dp[2])