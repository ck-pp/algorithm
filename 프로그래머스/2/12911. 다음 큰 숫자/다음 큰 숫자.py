def solution(n):
    bin_n_one = bin(n).count('1')
    for next in range(n+1, n * 2 + 1):
        if bin(next).count('1') == bin_n_one:
            return next