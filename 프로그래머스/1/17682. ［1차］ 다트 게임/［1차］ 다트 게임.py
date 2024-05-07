import re

def solution(dartResult):
    pow_d = {'S':1, 'D':2, 'T':3}
    num = re.sub('(S|D|T|\*|#)', ' ', dartResult).split(' ')
    new_d = ''.join(ch for ch in dartResult if not ch.isnumeric())
    st = [int(n) for n in num if n != '']
    op = -1
    for ch in new_d:
        if ch in ['S', 'D', 'T']:
            op += 1
            st[op] = pow(st[op], pow_d[ch])
        elif ch == '#':
            st[op] = st[op]*(-1)
        else:
            st[op] = st[op]*2
            if op > 0:
                st[op-1] = st[op-1]*2
            
    return sum(st)