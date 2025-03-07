import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))
dp = [1] * n  # 각 박스마다 한 번에 넣을 수 있는 최대의 상자 개수

for i in range(1, n):
    nums = []  # 현재 박스보다 앞에 있고, 크기가 작은 박스의 총 담긴 개수 저장
    for j in range(i-1, -1, -1):
        # 현재 박스보다 작은 크기의 박스를 만난 경우
        if boxes[i] > boxes[j]:
            nums.append(dp[j])
        
    # 현재 박스 수에 작은 크기 박스 중 가장 많은 총 박스 수를 더한다.
    if nums:
        dp[i] += max(nums)

# 한 줄에 넣을 수 있는 최대의 상자 개수 출력
print(max(dp))