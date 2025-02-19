import sys
input = sys.stdin.readline

N = 8  # 체스판 크기: 8x8
# (0, 0): 하얀칸, (0, 짝수), (1, 홀수), (2, 짝수), ...
chessBoard = [list(input().strip()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if (i + j) % 2 == 0:  # 하얀 칸일 경우((홀, 홀) 또는 (짝, 짝))
            if chessBoard[i][j] == 'F':  # 말이 존재하는 경우
                ans += 1

# 하얀 칸 위에 말이 몇 개 있는지 출력
print(ans)