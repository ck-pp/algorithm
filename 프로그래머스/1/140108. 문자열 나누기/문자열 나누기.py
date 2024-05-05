def solution(s):
    ans = 0
    same = []
    diff = []
    s_list = list(s)
    
    for ch in s:
        if not same or same[-1] == ch:
            same.append(s_list.pop(0))
        else:
            diff.append(s_list.pop(0))
        if len(same) == len(diff):
            ans += 1
            same.clear()
            diff.clear()
    if same:
        ans += 1
    return ans