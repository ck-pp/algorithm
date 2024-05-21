def solution(n):
    if n ** (1/2) - int(n ** (1/2)) == 0:
        return (n ** (1/2) +1) ** 2
    return -1