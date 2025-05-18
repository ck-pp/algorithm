from collections import deque

def solution(n):
    ans = 0
    q = deque([])
    sum_q = 0
    
    for i in range(1, n + 1):
        q.append(i)
        sum_q += i
        
        if sum_q > n:
            while sum_q > n:
                sum_q -= q.popleft()
                
        if sum_q == n:
            ans += 1
                
    return ans