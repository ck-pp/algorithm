import sys
input = sys.stdin.readline

N = int(input())
facto = 1

for i in range(2, N+1):
    facto *= i

print(facto)
    