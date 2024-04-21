def solution(n):
    ans = 0
    n_next = n+1
    bin_n_one = bin(n).count('1')
    while True:
        if bin(n_next).count('1') == bin_n_one:
            return n_next
        else:
            n_next += 1