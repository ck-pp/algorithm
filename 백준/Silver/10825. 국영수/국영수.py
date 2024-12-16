import sys
imput = sys.stdin.readline

N = int(input())
scores = [tuple(input().split()) for _ in range(N)]  # (이름, 국, 영, 수)

# 국어 내림차순 -> 영어 오름차순 -> 수학 내림차순 -> 이름 오름차순
scores.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name, _, _, _ in scores:
    print(name)