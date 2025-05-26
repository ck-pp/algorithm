def isSquareNumber(num):
    # 제곱수일 경우
    if num ** (1/2) - int(num ** (1/2)) == 0:
        return (int(num ** (1/2)) + 1) ** 2
    # 제곱수가 아닐 경우
    else:
        return -1
    
def solution(n):
    return isSquareNumber(n)