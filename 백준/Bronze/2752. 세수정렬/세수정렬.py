import sys
imput = sys.stdin.readline

nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

print(*sorted_nums)