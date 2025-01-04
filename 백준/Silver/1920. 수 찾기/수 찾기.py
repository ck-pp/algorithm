import sys
input = sys.stdin.readline

N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(1 if num in A else 0)