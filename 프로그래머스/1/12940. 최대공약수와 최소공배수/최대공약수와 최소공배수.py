import math

def solution(n, m):
    gcd_v = math.gcd(n, m)
    
    return [gcd_v, n * m // gcd_v]