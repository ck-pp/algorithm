def solution(n):
    return [x for x in range(2, n) if n % x == 1][0]