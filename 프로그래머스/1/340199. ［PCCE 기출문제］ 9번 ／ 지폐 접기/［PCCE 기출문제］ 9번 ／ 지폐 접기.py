def solution(wallet, bill):
    ans = 0
    min_b, max_b = min(bill), max(bill)
    min_w, max_w = min(wallet), max(wallet)
    while min_b > min_w or max_b > max_w:
        max_b //= 2
        if max_b < min_b:
            max_b, min_b = min_b, max_b
        ans += 1
        
    return ans