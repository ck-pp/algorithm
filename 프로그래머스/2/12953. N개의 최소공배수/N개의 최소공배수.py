import math

def solution(arr):
    lcm = arr[0] * arr[1] // math.gcd(arr[0], arr[1])  # 초기화
    
    for i in range(2, len(arr)):
        lcm = lcm * arr[i] // math.gcd(lcm, arr[i])
        
    return lcm