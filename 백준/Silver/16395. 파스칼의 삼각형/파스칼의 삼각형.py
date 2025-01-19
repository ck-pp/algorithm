import sys
input = sys.stdin.readline

n, k = map(int, input().split())

triangles = [0] + [[0] + [1] * i for i in range(1, n+2)]  # 0번째 값에 0을 추가함으로써 인덱스와 행/열을 맞춰준다.
for m in range(2, n+2):
    for n in range(2, m):  # 행의 양 끝의 값은 1
        triangles[m][n] = triangles[m-1][n-1] + triangles[m-1][n]
        
print(triangles[n][k])