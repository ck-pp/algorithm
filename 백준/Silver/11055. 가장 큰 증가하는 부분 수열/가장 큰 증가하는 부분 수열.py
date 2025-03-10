import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [num for num in A]  # 각 숫자마다 가장 큰 증가하는 부분 수열

# 가장 큰 증가하는 부분 수열 구하기
for i in range(1, n):
    nums = []
    for j in range(i-1, -1, -1):
        # 현재 숫자보다 작은 숫자를 만난 경우
        if A[i] > A[j]:
            nums.append(dp[j])
        
    # 현재 숫자 전까지 가장 큰 증가하는 부분 수열을 더한다.
    if nums:
        dp[i] += max(nums)

# 가장 큰 증가하는 부분 수열 길이 출력
print(max(dp))