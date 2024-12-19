import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

nums.sort()
i, j = 0, N-1
cnt = 0

while i < j:
    sum_v = nums[i] + nums[j]
    if sum_v == M:  # 두 재료의 고유한 번호의 합이 M인 경우(= 갑옷 만들어짐)
        cnt += 1
        i += 1
        j -= 1
    elif sum_v < M:  # 번호 합이 M보다 작은 경우
        i += 1
    else:  # 번호 합이 M보다 큰 경우
        j -= 1
        
print(cnt)