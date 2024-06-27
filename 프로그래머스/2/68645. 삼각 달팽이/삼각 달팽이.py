def solution(n):
    ans = []
    triangle = [[0] * (i+1) for i in range(n)]
    
    num = 1
    x, y = -1, 0
    for i in range(n): # 한 변씩 체크
        for _ in range(i, n):
            if i % 3 == 0: # 아래로
                x += 1
            elif i % 3 == 1: # 오른쪽으로
                y += 1
            else: # 대각선 위로
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    
    for row in triangle:
        ans.extend(row)
    
    return ans