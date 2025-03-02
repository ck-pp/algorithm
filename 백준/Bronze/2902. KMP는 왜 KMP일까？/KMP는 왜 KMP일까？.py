import sys
input = sys.stdin.readline

name = input().strip().split('-')  # '-' 기준으로 나눠서 저장
N = len(name)
short_name = ''

for i in range(N):
    # 각 성의 첫 글자만 저장
    short_name += name[i][0]
 
# 짧은 형태 이름 출력  
print(short_name)