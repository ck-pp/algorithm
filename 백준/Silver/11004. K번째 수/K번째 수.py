import sys
imput = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
print(sorted_nums[K-1])