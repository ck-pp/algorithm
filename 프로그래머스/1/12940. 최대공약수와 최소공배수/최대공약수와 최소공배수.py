def solution(n, m):
    ans = []
    mult = n * m
    # GCD / LCM = n*m // GCD
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    gcd = m
    lcm = mult // gcd
    return [gcd, lcm]