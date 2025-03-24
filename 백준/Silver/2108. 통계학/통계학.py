import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = list(int(input()) for _ in range(N))
nums.sort()  # 오름차순 정렬

num_cnt = Counter(nums)
# value(= cnt) 기준 오름차순 정렬, key(= num) 기준 내림차순 정렬
sorted_dict = sorted(num_cnt.items(), key= lambda item:(item[1], -item[0]))

# 1. 산술평균 출력
print(round(sum(nums) / N))

# 2. 중앙값 출력
print(nums[N // 2])

# 3. 최빈값 출력
# 여러 개 있을 경우 최빈값 중 두 번째로 작은 값 출력
if len(sorted_dict) > 1 and sorted_dict[-1][1] == sorted_dict[-2][1]:
    print(sorted_dict[-2][0])
else:
    print(sorted_dict[-1][0])

# 4. 범위 출력
print(nums[-1] - nums[0])