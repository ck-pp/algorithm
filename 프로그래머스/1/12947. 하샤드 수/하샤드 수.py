def solution(x):
    sum_n = sum([int(n) for n in str(x)])
    return x % sum_n == 0