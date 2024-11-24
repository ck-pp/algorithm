import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

dp = [num for num in nums]
for i in range(1, len(dp)):
    dp[i] = max(dp[i-1] + dp[i], dp[i])

print(max(dp))