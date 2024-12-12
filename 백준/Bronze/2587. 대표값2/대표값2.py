import sys
imput = sys.stdin.readline

nums = list(int(input()) for _ in range(5))
sorted_nums = sorted(nums)
sum_nums = sum(nums)

print(sum_nums // 5)
print(sorted_nums[2])