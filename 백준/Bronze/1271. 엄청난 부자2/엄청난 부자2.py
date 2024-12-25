import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(n // m)  # 한 명당 가지는 돈(= 몫)
print(n % m)  # 나눌 수 없는 돈(= 나머지)