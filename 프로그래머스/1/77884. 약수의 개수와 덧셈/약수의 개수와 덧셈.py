def factorNum(num):  # 약수 개수 반환 함수
    cnt = 0
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:  # 약수
            if num // i != i:  # 제곱수가 아닌 경우
                cnt += 2
            else:  # 제곱수인 경우
                cnt += 1
    
    return cnt % 2 == 0

def solution(left, right):
    # 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 빼기
    return sum(n if factorNum(n) else -n for n in range(left, right+1))
        