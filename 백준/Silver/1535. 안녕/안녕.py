import sys
input = sys.stdin.readline

N = int(input())  # 사람 수
L = [0] + list(map(int, input().split()))  # 각 사람으로부터 잃는 체력
J = [0] + list(map(int, input().split()))  # 각 사람으로부터 얻는 기쁨

# 체력이 hp일 때 얻을 수 있는 최대 기쁨(사람 기준이 아니라 체력 기준으로 인덱스를 잡아야 함)
dp = [0] * 101  # 체력은 최대 100까지

for i in range(1, N+1):
    for hp in range(100, L[i], -1):  # 체력 감소는 뒤에서부터 처리
        dp[hp] = max(dp[hp], dp[hp - L[i]] + J[i])

print(max(dp))