import sys
import math
input = sys.stdin.readline

num1, num2 = map(int, input().split())

# 1. 최대공약수 출력
print(math.gcd(num1, num2))
# 2. 최소공배수 출력
print(math.lcm(num1, num2))