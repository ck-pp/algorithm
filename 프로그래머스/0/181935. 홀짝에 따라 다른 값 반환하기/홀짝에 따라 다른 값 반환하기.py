def solution(n):
    ans = 0
    for i in range(1, n+1):
        if i % 2 == n % 2:
            ans += (i ** 2 if i % 2 == 0 else i)
    return ans