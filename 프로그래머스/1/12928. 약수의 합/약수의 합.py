def solution(n):
    ans = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            ans += i
            if i != n//i:
                ans += (n//i)
    return ans