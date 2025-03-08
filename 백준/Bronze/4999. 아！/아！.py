import sys
input = sys.stdin.readline

s1 = input().strip()  # 재환이가 낼 수 있는 소리 최대 길이
s2 = input().strip()  # 의사가 요구하는 소리 길이

if len(s1) >= len(s2):
    print("go")
else:
    print("no")