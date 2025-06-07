import math

def solution(n, m):
    gcd_v = math.gcd(n, m)
    lcm_v = n * m // gcd_v
    
    return [gcd_v, lcm_v]