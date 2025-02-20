import sys
input = sys.stdin.readline

n = int(input())  # N의 약수의 개수
divisors = list(map(int, input().split()))  # N의 진짜 약수(1, N 제외)

# 1. 오름차순 정렬
divisors.sort()

# 2. N 출력
if n % 2 == 0:  # 약수의 짝이 다 존재할 경우
    print(divisors[0] * divisors[-1])
else:  # 약수 중에 제곱수가 있을 경우
    print(divisors[n//2] ** 2)