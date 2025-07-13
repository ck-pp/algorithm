def solution(A,B):
    n = len(A)
    
    # 큰 값  * 작은 값 누적 합 = 최소
    A.sort()  # 오름차순 정렬
    B.sort(reverse=True)  # 내림차순 정렬
    
    return sum(A[i] * B[i] for i in range(n))