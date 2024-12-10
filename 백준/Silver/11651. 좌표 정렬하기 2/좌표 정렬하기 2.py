import sys
imput = sys.stdin.readline

N = int(input())
positions = [tuple(map(int, input().split())) for _ in range(N)]

# y좌표 기준 오름차순 정렬 -> x좌표 기준 오름차순 정렬
sorted_positions = sorted(positions, key=lambda x:(x[1], x[0]))

for x, y in sorted_positions:
    print(x, y)