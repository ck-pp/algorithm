import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    text = input().strip()
    converted_text = text[0].upper() + text[1:]  # 첫문자 -> 대문자로 변환
    
    print(converted_text)