import sys
import math
input = sys.stdin.readline

S = list(map(int, list(input().strip())))
stack = [S[0]]  # 첫번째 숫자(1 or 0)
cnt = 1  # 첫번째 연속된 숫자 구간 카운트

for i in range(len(S)):
    # 이전 숫자와 다를 경우
    if stack[-1] != S[i]:
        cnt += 1
    
    # 스택에 현재 숫자 추가
    stack.append(S[i])

# 다솜이가 해야하는 행동의 최소 횟수 출력
print(math.floor(cnt / 2))