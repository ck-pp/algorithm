import sys
input = sys.stdin.readline

S = input().strip()

alphas = [0] * 26  # a-z : 26글자
for s in S:
    # 아스키코드 a = 97 ~
    alphas[ord(s)-97] += 1
    
# 단어에 포함되어 있는 알파벳 개수 공백 구분 출력
print(*alphas)