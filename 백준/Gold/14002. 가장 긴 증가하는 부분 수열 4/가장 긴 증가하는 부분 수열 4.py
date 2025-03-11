import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp_len = [1 for _ in range(n)]  # 각 숫자마다 가장 긴 증가하는 부분 수열 길이
dp_arr = [[num] for num in A]  # 각 숫자마다 가장 긴 증가하는 부분 수열

# 가장 긴 증가하는 부분 수열 구하기
for i in range(1, n):
    max_nums = -1
    max_idx = -1
    for j in range(i-1, -1, -1):
        # 현재 숫자보다 작은 숫자를 만난 경우
        if A[i] > A[j] and max_nums < dp_len[j]:
            max_nums = dp_len[j]
            max_idx = j
        
    # 현재 숫자 전까지 가장 긴 증가하는 부분 수열을 더한다.
    if max_nums > -1:
        dp_len[i] += max_nums
        dp_arr[i].extend(dp_arr[max_idx])
    
# 가장 긴 증가하는 부분 수열 길이 출력
print(max(dp_len))
# 가장 긴 증가하는 부분 수열 출력
print(*reversed(dp_arr[dp_len.index(max(dp_len))]))