import sys
input = sys.stdin.readline

def is_palindrome(num, n):
    res = []
    # 10진수(num)를 n진수로 변환
    while num >= 1:
        res.append(str(num % n))
        num //= n
        
    # res는 n진수를 뒤집은 값
    return 1 if ''.join(res) == ''.join(list(reversed(res))) else 0
    
T = int(input())
for _ in range(T):
    num, n = map(int, input().split())
    
    print(is_palindrome(num, n))