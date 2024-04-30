import string

def solution(msg):
    ans = []
    st = []
    list_m = list(msg)
    dict = {alpha:idx+1 for idx, alpha in enumerate(string.ascii_uppercase)}
    cur_idx = len(dict)+1
    while len(list_m) > 0:
        if not st or (st and ''.join(st)+list_m[0] in dict.keys()):
            st.append(list_m.pop(0))
        else:
            ans.append(dict[''.join(st)])
            dict[''.join(st)+list_m[0]] = cur_idx
            st.clear()
            cur_idx += 1
    ans.append(dict[''.join(st)])
    return ans