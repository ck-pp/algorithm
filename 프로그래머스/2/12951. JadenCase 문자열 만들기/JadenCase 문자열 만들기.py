def solution(s):
    s_list = s.split(' ')
    
    for i in range(len(s_list)):
        up_st = low_st = ''
        if s_list[i] != '':
            up_st = s_list[i][0]
            if 'a' <= up_st <= 'z':
                up_st = s_list[i][0].upper()
            if len(s_list[i]) > 1:
                low_st = s_list[i][1:].lower()
        s_list[i] = up_st + low_st
        
    return ' '.join(s_list)