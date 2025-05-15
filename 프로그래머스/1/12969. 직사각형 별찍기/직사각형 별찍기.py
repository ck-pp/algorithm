import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(m):
    for _ in range(n):
        print('*', end='')
    print('')