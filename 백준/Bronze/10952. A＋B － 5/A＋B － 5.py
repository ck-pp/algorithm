import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    sum_AB = A + B
    if sum_AB == 0:
        break
    else:
        print(A + B)