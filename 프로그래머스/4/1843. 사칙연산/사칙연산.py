import sys

def solution(arr):
    INF = sys.maxsize
    NEG_INF = -sys.maxsize
    n = (len(arr) + 1) // 2  # 숫자의 개수
    dp_min = [[0] * n for _ in range(n)]
    dp_max = [[0] * n for _ in range(n)]
    
    # 초기화: 숫자 자체는 dp_min, dp_max에서 최소/최대 값
    for i in range(n):
        dp_min[i][i] = int(arr[2 * i])
        dp_max[i][i] = int(arr[2 * i])
    
    for size in range(1, n):  # 부분문제 크기: size
        for i in range(n - size):
            j = i + size
            dp_min[i][j] = INF
            dp_max[i][j] = NEG_INF
            
            for k in range(i, j):
                # 더하기 연산: 양쪽의 값이 모두 클수록 최종 결과가 커짐
                # 빼기 연산: 왼쪽의 값이 크고 오른쪽의 값이 작을수록 결과가 커짐
                if arr[2*k + 1] == '+':
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                elif arr[2*k + 1] == '-':
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
        
    return dp_max[0][n-1]