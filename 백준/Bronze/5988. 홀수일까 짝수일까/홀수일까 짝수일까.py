import sys
input = sys.stdin.readline

N = int(input())

# 홀수, 짝수 판단 함수
def isEven(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

for _ in range(N):
    num = int(input())
    
    # 홀수인지 짝수인지 출력
    print(isEven(num))