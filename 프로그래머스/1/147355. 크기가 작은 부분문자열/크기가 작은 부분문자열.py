def solution(t, p):
    d_str = []
    np = len(p)
    for i in range(len(t) - np + 1):
        d_str.append(int(t[i:i+np]))
        
    d_str.sort(reverse=True)  # 내림차순 정렬
    n_dstr = len(d_str)
    for j in range(n_dstr):
        if d_str[j] <= int(p):
            return n_dstr - j