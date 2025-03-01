import sys
import re
input = sys.stdin.readline

while True:
    # 모두 소문자로 변환 후, '.',',','!','?' 기준으로 자르기(정규표현식 라이브러리 re 사용)
    s = re.split('[,|.|!|?| ]', input().strip().lower())
    cnt = 0
    finds = ['a', 'e', 'i', 'o', 'u']  # 모음 문자 리스트
    
    # 종료
    if len(s) == 1 and s[0] == '#':
        break
    
    # 모음 문자 개수 카운트
    for word in s:
        for i in range(len(word)):
            if word[i] in finds:
                cnt += 1
    
    # 모음의 개수 출력        
    print(cnt)