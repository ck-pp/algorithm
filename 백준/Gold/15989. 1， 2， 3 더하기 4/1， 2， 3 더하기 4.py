import sys
import heapq
input = sys.stdin.readline

T = int(input())

# 1. 입력에서 n의 최댓값을 찾기 위해 우선 입력을 모두 받는다.
arr = []
max_n = 0
for _ in range(T):
    n = int(input())
    arr.append(n)
    if n > max_n:
        max_n = n
        
# 2. dp 정의
# dp[i] = i를 1, 2, 3의 합으로 나타내는 조합의 개수
dp = [0] * (max_n + 1)
dp[0] = 1  # dp 값 계산을 위해 0을 만드는 방법은 1가지로 둔다.

# 3. 동전 교환(조합) 방식: order를 고려하지 않으려면 1,2,3 순으로 반복
for coin in [1, 2, 3]:
    for i in range(coin, max_n + 1):
        dp[i] += dp[i - coin]
        
# 4. 각 테스트 케이스 출력
for n in arr:
    print(dp[n])