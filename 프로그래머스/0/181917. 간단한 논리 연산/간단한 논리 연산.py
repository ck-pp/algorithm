def solution(x1, x2, x3, x4):
    # V: 하나라도 T이면 T, ㅅ: 둘 다 T여야 T
    return (x1 | x2) & (x3 | x4)