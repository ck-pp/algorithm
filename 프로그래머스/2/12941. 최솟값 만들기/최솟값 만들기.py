def solution(A,B):
    ans = 0
    n = len(A)
    
    # 큰 값  * 작은 값 누적 합 = 최소
    A.sort()  # 오름차순 정렬
    B.sort(reverse=True)  # 내림차순 정렬
    
    for i in range(n):
        ans += A[i] * B[i]
    
    return ans