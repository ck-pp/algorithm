from collections import deque

def solution(n):
    ans = 0
    q = deque([])  # 연속된 자연수 담을 큐(FIFO)
    sum = 0  # 현재 연속된 자연수 합
    
    for i in range(1, n + 1):
        q.append(i)
        sum += i
        if sum > n:  # 현재 연속된 자연수 합이 n보다 클 경우
            while sum > n:  # 작거나 같아질 때까지 작은 수부터 -
                sum -= q.popleft()
        if sum == n:  # 연속된 자연수 합이 n일 경우
            ans += 1    
    
    return ans