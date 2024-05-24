def solution(n):
    ans = 0
    for x in range(2, n):
        if (n-1) % x == 0:
            return x