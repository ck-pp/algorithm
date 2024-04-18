def solution(n, lost, reserve):
    l_r = list(set(lost) - set(reserve))
    r_l = list(set(reserve) - set(lost))
    ans = n - len(l_r)
    for i in range(1, len(r_l)+1):
        for j in range(1, len(l_r)+1):
            if r_l[-i]-1 <= l_r[-j] <= r_l[-i]+1:
                l_r.remove(l_r[-j])
                ans += 1
                break
    return ans