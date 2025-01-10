import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)  # 내림차순 정렬
    print(A[2])