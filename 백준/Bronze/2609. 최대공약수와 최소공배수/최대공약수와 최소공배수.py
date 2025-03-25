import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 1. 최대공약수 계산 함수 정의
def gcd(a, b):
    # 유클리드 알고리즘(호제법)
    while b > 0:
        a, b = b, a % b
    return a
    
# 2. 최소공배수 계산 함수 정의
def lcm(a, b):
    return a * b // gcd(a, b) 

# 1. 최대공약수 출력
print(gcd(num1, num2))
# 2. 최소공배수 출력
print(lcm(num1, num2))