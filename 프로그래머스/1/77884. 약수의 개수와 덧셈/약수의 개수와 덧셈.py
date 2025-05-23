# 약수 개수가 짝수인지 판별해주는 함수 (T/F)
def isFactorEven(num):
    factor_cnt = 0
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            factor_cnt += 2
            # 제곱수인 경우 약수 1개가 1쌍
            if i == num // i:
                factor_cnt -= 1
            
    return factor_cnt % 2 == 0

def solution(left, right):
    ans = 0
    for n in range(left, right + 1):
        if isFactorEven(n):
            ans += n
        else:
            ans -= n
            
    return ans
        