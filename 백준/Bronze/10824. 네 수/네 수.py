import sys
input = sys.stdin.readline

A, B, C, D = input().strip().split()
AB = int(A + B)
CD = int(C + D)

print(AB + CD)