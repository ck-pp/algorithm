import sys
input = sys.stdin.readline

word = input().strip()
vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for s in word:
    if s in vowels:
        cnt += 1
        
# 모음 개수 출력
print(cnt)