import sys
input = sys.stdin.readline

n = int(input())
# 시작 시점 점수 = 100
c_total_score, s_total_score = 100, 100

for _ in range(n):
    c_score, s_score = map(int, input().split())
    
    # 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃는다.
    if c_score > s_score:
        s_total_score -= c_score
    if c_score < s_score:
        c_total_score -= s_score
        
print(c_total_score)  # 창영이의 점수 출력
print(s_total_score)  # 상덕이의 점수 출력