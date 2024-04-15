def solution(n):
    ans = 0
    i = 1
    while i <= n:
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                ans += 1
            elif sum > n:
                sum = 0
                break
        i += 1
    return ans