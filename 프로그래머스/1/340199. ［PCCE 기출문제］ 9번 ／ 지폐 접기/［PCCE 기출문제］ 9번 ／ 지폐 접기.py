def solution(wallet, bill):
    ans = 0
    wallet, bill = sorted(wallet), sorted(bill)
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        bill.sort()
        ans += 1
        
    return ans