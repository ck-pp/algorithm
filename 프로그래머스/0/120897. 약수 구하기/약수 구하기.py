def solution(n):
    ans = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            ans.extend([i, n // i])
            
    return sorted(set(ans))