from collections import deque

def solution(n):
    dq = deque([])
    cur_sum, ans = 0, 0
    for i in range(1, n+1):
        # 값 추가
        dq.append(i)
        cur_sum += i
        
        # 연속한 자연수들의 합이 n보다 큰 경우
        while cur_sum > n:
            cur_sum -= dq.popleft()
        
        ## 연속한 자연수들의 합이 n인 경우 카운트
        if cur_sum == n:
            ans += 1
            
    return ans