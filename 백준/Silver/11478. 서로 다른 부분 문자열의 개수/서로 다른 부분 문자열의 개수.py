import sys
input = sys.stdin.readline

S = input().strip()
substring = set(list(S))  # 부분 문자열 저장 집합(중복 제거 위해)
n = len(S)

for i in range(2, n+1):
    for j in range(n-i + 1):
        substring.add(S[j:j+i])  # 문자열 슬라이싱
        
# 부분 문자열 개수 출력
print(len(substring))