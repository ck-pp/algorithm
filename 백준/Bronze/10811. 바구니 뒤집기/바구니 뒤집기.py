import sys
input = sys.stdin.readline

N, M = map(int, input().split())
i_j_lists = [list(map(int, input().split())) for _ in range(M)]
buckets = [str(num) for num in range(N+1)]

for i, j in i_j_lists:
    buckets[i:j+1] = list(reversed(buckets[i:j+1]))
    
print(' '.join(buckets[1:]))