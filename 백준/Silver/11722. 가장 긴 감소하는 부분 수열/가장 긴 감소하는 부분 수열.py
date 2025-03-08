import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [1] * n  # 각 숫자마다 가장 긴 감소하는 부분 수열

# 끝에서부터 가장 긴 증가하는 부분 수열 구하기(= 뒤집어서 생각)
for i in range(n-1, -1, -1):
    nums_len = []
    for j in range(i+1, n):
        # 현재 숫자보다 작은 숫자를 만난 경우
        if A[i] > A[j]:
            nums_len.append(dp[j])
        
    # 현재 숫자 전까지 가장 긴 감소하는 부분 수열을 더한다.
    if nums_len:
        dp[i] += max(nums_len)

# 가장 긴 감소하는 부분 수열의 길이 출력
print(max(dp))