def solution(board, h, w):
    cnt = 0
    n = len(board)
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in move:
        dh, dw = (h + d[0]), (w + d[1])
        if (0 <= dh < n and 0 <= dw < n):
            if (board[h][w] == board[dh][dw]):
                cnt += 1

    return cnt