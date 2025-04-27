import sys
from collections import Counter
input = sys.stdin.readline

# 대소문자 구분X and 가장 많이 사용된 알파벳을 대문자로 출력
word = input().strip().upper()

# 1. 사용된 알파벳과 횟수를 딕셔너리로 저장
alpha_cnt = Counter(word)

# 2. 사용된 횟수(value) 기준 내림차순 정렬
sorted_alpha = sorted(alpha_cnt.items(), key=lambda item:-item[1])

# 3. 단어 길이가 1이거나 많이 사용된 알파벳이 1가지일 경우
n = len(sorted_alpha)
if n == 1 or (n > 1 and sorted_alpha[0][1] != sorted_alpha[1][1]):
    print(sorted_alpha[0][0])
else:
    print('?')