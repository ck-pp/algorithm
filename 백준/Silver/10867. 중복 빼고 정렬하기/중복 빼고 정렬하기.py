import sys
input = sys.stdin.readline

N = int(input())
nums = list(set(map(int, input().split())))

nums.sort()
print(*nums)