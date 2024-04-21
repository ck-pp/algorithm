def solution(n):
    ans = 0
    n_next = n+1
    bin_n_one = str(bin(n))[2:].count('1')
    while True:
        if str(bin(n_next))[2:].count('1') == bin_n_one:
            return n_next
        else:
            n_next += 1