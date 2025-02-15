import sys
input = sys.stdin.readline

# 1. 펠린드롬수인지 판단하는 함수
def is_palindrome(s):
    n = len(s)
    for i in range(len(s) // 2):
        if s[i] != s[n-i-1]:
            return "no"
    
    return "yes"
        
while True:
    s = input().strip()
    
    # 0을 입력받으면 반복문 종료
    if s == '0':
        break
    
    # 2. 팰린드롬수면 'yes', 아니면 'no' 출력
    print(is_palindrome(s))