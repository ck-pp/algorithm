import sys
input = sys.stdin.readline

A_length, B_length = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A - B
B_A = B - A
print(len(A_B.union(B_A)))