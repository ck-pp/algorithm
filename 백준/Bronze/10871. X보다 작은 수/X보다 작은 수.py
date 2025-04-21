import sys
input = sys.stdin.readline

N, X = map(int, input().split())
nums = list(map(int, input().strip().split()))

ans = []
for num in nums:
    if num < X:
        ans.append(num)
        
print(' '.join(map(str, ans)))