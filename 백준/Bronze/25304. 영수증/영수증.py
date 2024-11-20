import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

sum_price = 0
for _ in range(N):
    obj, price = map(int, input().split())
    sum_price += obj * price

print("Yes" if sum_price == X else "No")