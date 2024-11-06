import sys

N, k = map(int, sys.stdin.readline().split())
scores = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

print(scores[k-1])