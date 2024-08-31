import math

def solution(numer1, denom1, numer2, denom2):
    lcm = int(denom1 * denom2 / math.gcd(denom1, denom2))
    numer = (numer1 * lcm // denom1) + (numer2 * lcm // denom2)
    return [numer // math.gcd(numer, lcm), lcm // math.gcd(numer, lcm)]