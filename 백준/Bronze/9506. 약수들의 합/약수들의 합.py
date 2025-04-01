import sys
input = sys.stdin.readline

# (완전수인지 T/F, 약수 리스트) 반환 함수
def divisor_arr(num):
    divisors = []
    sum_divisors = 0
    
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            divisors.append(i)
            sum_divisors += i
            # 제곱수일 경우 중복 방지
            if num // i not in divisors and num // i != num:
                divisors.append(num // i)
                sum_divisors += (num // i)
    # 완전수일 경우
    if sum_divisors == num:
        divisors.sort()  # 약수들 오름차순 정렬
        return [True, divisors]
    # 완전수가 아닐 경우
    else:
        return [False, divisors]

while True:
    N = int(input())
    
    if N == -1:
        break
    
    is_perfect_number, divisors = divisor_arr(N)
    
    # 완전수일 경우
    if is_perfect_number:
        print(str(N) + " = ", end='')
        for j in range(len(divisors) - 1):
            print(str(divisors[j]) + " + ", end='')
        print(divisors[-1])
        
    # 완전수가 아닐 경우
    else:
        print(str(N) + " is NOT perfect.")