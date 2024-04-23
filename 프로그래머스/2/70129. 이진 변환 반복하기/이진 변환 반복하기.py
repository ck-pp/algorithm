def solution(s):
    cnt_t = 0
    cnt_0 = 0
    while s != '1':
        cnt_0 += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt_t += 1
    return [cnt_t, cnt_0]