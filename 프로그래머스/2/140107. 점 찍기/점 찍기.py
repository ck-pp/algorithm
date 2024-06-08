def solution(k, d):
    ans = 0
    for a in range(0, d+1, k):
        b = 0
        max_v = (d**2 - a**2) - (d**2 - a**2)%k
        ans += (int(max_v**(0.5)) // k + 1)
    
    return ans