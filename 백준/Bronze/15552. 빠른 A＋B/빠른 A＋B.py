import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num1, num2 = map(int, input().split())
    
    print(num1 + num2)