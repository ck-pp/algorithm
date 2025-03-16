import sys
input = sys.stdin.readline

A, B = map(int, input().split())  # 시, 분
C = int(input())  # 요리에 필요한 시간

# 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수
A += (C // 60)
B += (C % 60)

if B > 59:
    A += 1
    B -= 60
if A > 23:
    A -= 24
    
# 종료되는 시각의 시와 분 출력
print(A, B)