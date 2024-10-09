def solution(A, B):
    ans = 0
    sort_A, sort_B = sorted(A, reverse=True), sorted(B, reverse=True)
    b_idx = 0
    for a in sort_A:
        if sort_B[b_idx] > a:
            ans += 1
            b_idx += 1
            
    return ans