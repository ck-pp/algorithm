import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    alphas = input().strip().split()
    
    ans = deque([alphas[0]])
    for i in range(1, N):
        if alphas[i] <= ans[0]:  # 앞에 놓인 카드들 가장 왼쪽에 놓아야 하는 경우
            ans.appendleft(alphas[i])
        else:  # 앞에 놓인 카드들 가장 오른쪽에 놓아야 하는 경우
            ans.append(alphas[i])
            
    # 사전 순으로 가장 빠른 문자열 출력
    print(''.join(ans))