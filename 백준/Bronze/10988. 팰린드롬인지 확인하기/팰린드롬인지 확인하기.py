import sys
from collections import deque
input = sys.stdin.readline

string = deque(list(input().strip()))
is_palindrome = True  # 기본값은 True로 설정

while len(string) > 1:  # 홀수 길이인 경우에는 1글자 남을때까지만, 짝수 길이인 경우에는 모두 pop
    left_s = string.popleft()
    right_s = string.pop()
    
    if left_s != right_s:
        is_palindrome = False
        break

# 남은 문자 개수가 2개 이상일 경우 팰린드롬이 아님
print(1 if is_palindrome else 0)