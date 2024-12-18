import sys
from collections import deque
imput = sys.stdin.readline

def get_primes():
    primes = [True] * 10000  # 네자리수로 제한되어 있으므로
    primes[0] = primes[1] = False
    for i in range(2, int(10000 ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, 10000, i):  # 에라토스테네스의 체의 원리: 소수의 배수는 소수가 아님.
                primes[j] = False
                
    return primes
    
def generate_next_nums(cur_num, primes):
    cur_num = list(cur_num)
    next_nums = []
    
    for i in range(4):
        origin_digit = cur_num[i]
        for digit in "0123456789":
            if i == 0 and digit == '0':  # 첫번째 자리는 1-9 가능
                continue
            if digit == origin_digit:  # 변환 안했을때
                continue
            
            cur_num[i] = digit  # 자리수 변환
            new_num = int(''.join(cur_num))
            
            # 네 자리 소수인 숫자만 후보에 추가
            if primes[new_num]:
                next_nums.append(str(new_num))
                
        cur_num[i] = origin_digit
        
    return next_nums

T = int(input())
primes = get_primes()
for _ in range(T):
    start, end = input().split()
    q = deque([(0, start)])  # (변환 횟수, 숫자)
    visited = set([start])
    
    # 첫번째 자리수 != 0
    while q:
        steps, cur_num = q.popleft()
        
        if cur_num == end:
            print(steps)
            break
        
        for next_num in generate_next_nums(cur_num, primes):
            if next_num not in visited:
                visited.add(next_num)
                q.append((steps + 1, next_num))
        
    else:
        print("Impossible")