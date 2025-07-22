def solution(s):
    ans = []
    cur_pos = {}
    for i in range(len(s)):
        if s[i] not in cur_pos:
            ans.append(-1)
            cur_pos[s[i]] = i
        else:
            ans.append(i - cur_pos[s[i]])
            cur_pos[s[i]] = i
                
    return ans