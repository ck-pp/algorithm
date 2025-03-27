import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# nCk == nCn-k
if K > N - K:
    K = N - K
    
numerator, denominator = 1, 1
# 1. 분자 계산
for i in range(N, N-K, -1):
    numerator *= i
    
# 2. 분모 계산
for j in range(1, K+1):
    denominator *= j

# 이항계수(= nCk) 출력
print(numerator // denominator)
