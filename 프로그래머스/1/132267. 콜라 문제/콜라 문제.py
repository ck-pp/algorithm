def solution(a, b, n):
    ans = 0
    while n >= a:
        new_coke = (n // a) * b
        ans += new_coke
        n = new_coke + n % a
        
    return ans