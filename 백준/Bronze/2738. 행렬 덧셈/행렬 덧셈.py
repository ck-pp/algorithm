import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix_A = [list(map(int, input().split())) for _ in range(N)]
matrix_B = [list(map(int, input().split())) for _ in range(N)]

# 행렬 A와 B를 더한 행렬 출력
for i in range(N):
    for j in range(M):
        print(matrix_A[i][j] + matrix_B[i][j], end=' ')
    print('')