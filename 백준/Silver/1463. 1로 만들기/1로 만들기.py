import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)  # dp[i]는 i를 만들기 위한 최소 연산 횟수
q = deque([N])  # BFS 큐

while q:
    cur_num = q.popleft()
    
    # 1에 도달한 경우
    if cur_num == 1:
        break
    
    # 가능한 연산
    if cur_num % 3 == 0 and dp[cur_num // 3] == 0:
        dp[cur_num // 3] = dp[cur_num] + 1
        q.append(cur_num // 3)
    if cur_num % 2 == 0 and dp[cur_num // 2] == 0:
        dp[cur_num // 2] = dp[cur_num] + 1
        q.append(cur_num // 2)
    if dp[cur_num - 1] == 0:
        dp[cur_num - 1] = dp[cur_num] + 1
        q.append(cur_num - 1)
    
# 1에 도달하기 위한 최소 연산 횟수
print(dp[1])