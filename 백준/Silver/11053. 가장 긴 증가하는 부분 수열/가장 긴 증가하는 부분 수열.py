import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# dp[i]: 수열의 i번쨰 원소를 끝으로 하는 가장 긴 증가하는 부분 수열 길이
dp = [1] * N  # 자기 자신을 모두 가지므로 1로 초기화
for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))