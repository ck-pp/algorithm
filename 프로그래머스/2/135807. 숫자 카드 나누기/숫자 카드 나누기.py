import math

def gcd(arr):
    gcd_v = arr[0]
    for i in range(len(arr)):
        gcd_v = math.gcd(gcd_v, arr[i])
    return gcd_v
        
def isDivided(num, arr):
    for n in arr:
        if n % num == 0:
            return 0
    return num

def solution(arrayA, arrayB):
    a_div = isDivided(gcd(arrayB), arrayA)
    b_div = isDivided(gcd(arrayA), arrayB)
    # 한쪽 카드 내에서 최대공약수 구함
    # 오름차순 정렬이므로 최대공약수는 첫 번째 원소보다 클 수 x
    # 최대공약수가 모든 약수를 포함하고 있기 때문에 최대공약수만 다른 카드 내에서 나눠지는지 확인하면 됨
    return max(a_div, b_div)