def solution(keymap, targets):
    ans = []
    key_m = {key:101 for key in ''.join(keymap)}
    
    for km in keymap:
        for k in range(len(km)):
            if k+1 < key_m[km[k]]:
                key_m[km[k]] = k+1
                
    for target in targets:
        sum = 0
        for t in target:
            if key_m.get(t):
                sum += key_m[t]
            else:
                sum = -1
                break
        ans.append(sum)
        
    return ans