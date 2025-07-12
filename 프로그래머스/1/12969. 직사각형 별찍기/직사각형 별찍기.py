import sys
input = sys.stdin.readline
n, m = map(int, input().split())

[print('*' * n) for _ in range(m)]

