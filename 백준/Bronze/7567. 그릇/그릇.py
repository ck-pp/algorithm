import sys
input = sys.stdin.readline

plates = list(input().strip())
height = 10

for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:  # 그릇이 같은 방향으로 포개진 경우
        height += 5
    else:  # 그릇이 서로 반대 방향으로 포개진 경우
        height += 10
      
# 쌓인 그릇의 최종 높이
print(height)